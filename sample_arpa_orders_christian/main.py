import os
import fitz  # PyMuPDF
import pandas as pd

def analyze_pdfs(main_folder_path, output_excel_path):
    all_results = []
    quality_scores = {}

    # Iterate through all subfolders inside the main folder
    for secondary_folder_name in os.listdir(main_folder_path):
        secondary_folder_path = os.path.join(main_folder_path, secondary_folder_name)

        # Check if it is a directory
        if os.path.isdir(secondary_folder_path):
            # Iterate through all PDF files in the secondary folder
            for pdf_file in os.listdir(secondary_folder_path):
                if pdf_file.endswith('.pdf'):
                    pdf_path = os.path.join(secondary_folder_path, pdf_file)
                    doc = fitz.open(pdf_path)
                    total_words_per_pdf = 0
                    total_pages = len(doc)

                    # Iterate through each page in the PDF
                    for page_num in range(total_pages):
                        page = doc[page_num]
                        text = page.get_text()

                          # Create or open the output text file
                        with open("small_sample.txt", 'w', encoding='utf-8') as output_file:
                            output_file.write(text)
               


                        # Calculate text metrics for the page
                        total_text = len(text)
                        total_words = len(text.split())
                        non_readable_text = sum(1 for char in text if not char.isprintable())

                        # Determine if the page is scanned or digital based on image content
                        is_scanned = page.get_images(full=True)
                        page_type = "Scanned" if is_scanned else "Digital"

                        # Store results for each page
                        all_results.append({
                            "Main Folder Name": os.path.basename(main_folder_path),
                            "Secondary Folder Name": secondary_folder_name,
                            "PDF Name": pdf_file,
                            "Page Number": page_num + 1,
                            "Total Words": total_words,
                            "Total Text Length (characters)": total_text,
                            "Non-readable Characters": non_readable_text,
                            "Page Type": page_type
                        })

                        total_words_per_pdf += total_words

                    # Calculate a readability score for the PDF (adjust formula if necessary)
                    quality_score = total_words_per_pdf / total_pages if total_pages > 0 else 0
                    quality_scores[f"{secondary_folder_name}/{pdf_file}"] = {
                        "Main Folder Name": os.path.basename(main_folder_path),
                        "Secondary Folder Name": secondary_folder_name,
                        "PDF Name": pdf_file,
                        "Total Pages": total_pages,
                        "Total Words": total_words_per_pdf,
                        "Quality Score": quality_score
                    }

                    doc.close()

    # Create a DataFrame with the results per page
    df_details = pd.DataFrame(all_results)

    # Create a DataFrame with the quality scores for each PDF
    df_quality = pd.DataFrame.from_dict(quality_scores, orient='index')

    # Export DataFrames to an Excel file with two sheets
    with pd.ExcelWriter(output_excel_path) as writer:
        df_details.to_excel(writer, sheet_name='Page Details', index=False)
        df_quality.to_excel(writer, sheet_name='Quality Scores', index=True)

    return df_details, df_quality

main_folder_path = 'AO_0001_small'  # Replace with the correct path of your main folder
output_excel_path = 'output_results_small.xlsx'
df_details, df_quality = analyze_pdfs(main_folder_path,output_excel_path)