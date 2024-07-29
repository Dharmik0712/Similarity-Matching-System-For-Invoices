# Similarity-Matching-System-For-Invoices
# Document Similarity Matching System

## Project Overview

This project aims to develop a document similarity matching system for invoices. The system takes an input invoice in PDF format and compares it to a database of existing invoices. The goal is to identify the most similar invoice in the database based on content and structural similarity.

## Approach

### Document Representation

1. Text Extraction: 
   - We use the `PyPDF2` library to extract text content from PDF files. This involves reading the PDF file and converting its content into a textual representation.

2. Feature Extraction: 
   - From the extracted text, we focus on relevant features such as keywords, invoice numbers, dates, and amounts. These features help in comparing the content of different invoices.

# Similarity Calculation

1. Cosine Similarity: 
   - We use cosine similarity to compare the textual content of invoices. Cosine similarity measures the cosine of the angle between two non-zero vectors in a multidimensional space, which in this case are the feature vectors of the invoices.

# File Structure
- `main.py`: The main script to run the application.
- `extract_text.py`: Contains the function to extract text from PDF files.
- `similarity.py`: Contains the function to calculate similarity between documents.
- `database.py`: Sets up the in-memory database of invoices.
- `README.md`: This documentation file.
- `invoices`: Directory where existing invoices are stored.

# How to Run the Code

# Prerequisites
- Python 3.6 or higher
- The following Python libraries:
  - PyPDF2
  - scikit-learn
  - tfIdfInheritVectorizer
  
# Setup Instructions

1. Clone the Repository:
   ```sh
   git clone https://github.com/yourusername/DeepLogicAI_Task.git
   cd DeepLogicAI_Task

2. Install Dependencies:

-> pip install PyPDF2 scikit-learn
-> pip install tfIdfInheritVectorizer
   
3. Add Sample Invoices:
Place your existing invoices (PDF files) in the directory.
Place the sample invoice you want to compare in the invoices/directory.

## Explanation of Code

-main.py:-
->Function: This is the main entry point of the application. It loads the database, extracts text from the input PDF, calculates similarity with existing invoices, and prints the results.

-extract_text.py:-
->Function: This file contains the extract_text_from_pdf() function, which uses the PyPDF2 library to extract text from PDF files.

-similarity.py:-
->Function: This file contains the calculate_similarity() function. It uses cosine similarity to compare the text content of invoices.

-database.py:-
->Function: This file sets up our in-memory database. The get_invoices() function loads existing invoices into memory for comparison.

-Further Improvements:-
->Optimization: Optimizing the similarity algorithm for better performance.
->Database Support:- Adding more robust database support for storing and retrieving invoices.
->GUI: Developing a graphical user interface for easier interaction with the system.

-Contact:-
For any questions or further information, feel free to contact me at [dharmiksompura1212@gmail.com] .
