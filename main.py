import os
from extract_text import extract_text_from_pdf
from feature_extraction import extract_features
from similarity import calculate_similarity
from database import init_db, add_invoice, get_all_invoices

def main():
    init_db()
    file_name = ''
    directory = 'invoices'
    current_directory = os.getcwd()
    for item in os.listdir(current_directory):
        if file_name.endswith('.pdf'):
            file_path = os.path.join(directory, file_name)
            text = extract_text_from_pdf(file_path)
            add_invoice(file_name, text)
    
    input_file = 'input_invoice.pdf'
    input_text = extract_text_from_pdf(input_file)
    
    best_match = None
    highest_similarity = 0
    
    for file_name, content in get_all_invoices():
        similarity = calculate_similarity(input_text, content)
        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = file_name
    
    if best_match:
        print(f"The most similar invoice is: {best_match} with a similarity score of {highest_similarity}")
    else:
        print("No similar invoice found.")

if __name__ == '__main__':
    main()
