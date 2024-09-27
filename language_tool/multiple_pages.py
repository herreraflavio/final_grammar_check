
import language_tool_python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import os

# Initialize LanguageTool once
tool = language_tool_python.LanguageTool('en-US')

def get_grammar_score(text, tool):
    # Start time tracking
    start_time = time.time()
    
    # Check the text for grammar errors
    matches = tool.check(text)
    
    # Count the number of errors
    num_errors = len(matches)
    num_words = len(text.split())
    
    # Calculate grammar score as (1 - errors/words) * 100
    grammar_score = (1 - num_errors / num_words) * 100 if num_words > 0 else 100
    
    # End time tracking and calculate elapsed time in milliseconds
    elapsed_time_ms = (time.time() - start_time) * 1000  # Convert seconds to milliseconds
    
    return grammar_score, num_errors, elapsed_time_ms

# Function to process multiple texts in parallel and calculate average time
def process_texts_in_parallel(texts):
    total_time = 0
    num_files = len(texts)

    with ThreadPoolExecutor(max_workers=24) as executor:  # Adjust `max_workers` based on your CPU cores
        futures = {executor.submit(get_grammar_score, text, tool): i for i, text in enumerate(texts, 1)}
        for future in as_completed(futures):
            index = futures[future]
            score, errors, time_taken = future.result()

            print(f"File {index} Grammar Score: {score:.2f}%")
            print(f"File {index} Number of Errors: {errors}")
      
            
            # Add time taken for each file to the total
            total_time += time_taken
    
    # Calculate and print average time taken
    average_time = total_time / num_files if num_files > 0 else 0
    print(f"Average Time Taken: {average_time:.2f} ms")

# Function to read all .txt files from a folder
def load_texts_from_files(directory):
    texts = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                texts.append(file.read())  # Read the content of each text file
    return texts

# Directory where the .txt files are located
# directory_path = "txtfiles_test"  # Replace this with your directory path
directory_path = "../txt_files/"  # Replace this with your directory path

# Load texts from files in the directory
texts = load_texts_from_files(directory_path)

# Process texts and print results as soon as each task completes
process_texts_in_parallel(texts)

# Close the LanguageTool instance to terminate the Java process
tool.close()
