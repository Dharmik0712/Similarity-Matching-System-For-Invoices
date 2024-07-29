from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def represent_documents(documents):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    return tfidf_matrix, vectorizer

def compute_similarity(tfidf_matrix, vectorizer, new_document):
    new_tfidf = vectorizer.transform([new_document])
    cosine_similarities = np.dot(tfidf_matrix, new_tfidf.T).toarray().flatten()
    return cosine_similarities
