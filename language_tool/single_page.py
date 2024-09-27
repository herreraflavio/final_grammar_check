import language_tool_python

def grammar_check(text):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)

    num_errors = len(matches)
    num_words = len(text.split())

    # Calculate a basic grammar score: (1 - errors/words) * 100 to get a percentage
    if num_words > 0:
        grammar_score = (1 - num_errors / num_words) * 100
    else:
        grammar_score = 100  # Perfect score for an empty string
    
    corrected_text = tool.correct(text)  # Get corrected text inside the function
    
    return grammar_score, matches, corrected_text

# Test the function with an example
# text = "This are a simple sentence with a grammar error."
with open("../txt_files/page_2.txt", 'r', encoding='utf-8', errors='replace') as file:
    text = file.read()


score, errors, corrected_text = grammar_check(text)

with open("output_text.txt", 'w', encoding='utf-8') as output_file:
    output_file.write(corrected_text)

print(f"Grammar Score: {score}%")
print(f"Number of Errors: {len(errors)}")

# Show the errors
for error in errors:
    print(f"Error: {error.ruleId}")
    print(f"Message: {error.message}")
    print(f"Suggested correction(s): {error.replacements}")
    print()

print("Corrected Text:", corrected_text)
