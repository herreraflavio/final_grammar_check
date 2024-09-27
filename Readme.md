# extract_text_from_pdfs.py extract text from each page using standard method (PyPDF2)

# ./language_tool contains single_page.py and multiple_pages.py

## https://languagetool.org/

## https://github.com/languagetool-org/languagetool

## single_page.py checks grammar score for one page and applies grammar corrections

## multiple_pages.py checks grammar score for multiple pages

# ./model contains grammar_correction_model.py

## grammar_correction_model.py uses vennify/t5-base-grammar-correction which is trained with Happy Transformer

## https://huggingface.co/vennify/t5-base-grammar-correction

## https://github.com/EricFillion/happy-transformer

## https://arxiv.org/abs/1702.04066

# Andrea shared https://github.com/hypothesis/pdf-text-quality

## got it working locally, however seems to be an issue with wsl and flags (pdf-text-quality seems to work though, not sure)
