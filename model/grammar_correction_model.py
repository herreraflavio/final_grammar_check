from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch

# Load the pre-trained T5 model and tokenizer for grammar correction
model = T5ForConditionalGeneration.from_pretrained('vennify/t5-base-grammar-correction')
tokenizer = T5Tokenizer.from_pretrained('vennify/t5-base-grammar-correction')

# Move the model to GPU if available
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

def correct_grammar(text):
    inputs = tokenizer.encode("fix: " + text, return_tensors="pt").to(device)
    outputs = model.generate(inputs, max_length=1024, num_beams=4, early_stopping=True)
    corrected_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return corrected_text

# Example usage
text = "Hello world.. This is bad a sentencee with many errors."
corrected = correct_grammar(text)
print(f"Corrected Text: {corrected}")
