def count_words_in_file(file_path):
    try:
        # Open the file and read its contents
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            # Split the text into words and count them
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return 0

# Example usage
file_path = 'example.txt'  # Replace with the path to your .txt file
word_count = count_words_in_file("sample.txt")
print(f"The number of words in the file is: {word_count}")
