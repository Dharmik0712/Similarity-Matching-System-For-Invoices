import re

def extract_features(text):
    features = {}
    features['invoice_number'] = re.search(r'Invoice Number:\s*(\S+)', text).group(1)
    features['date'] = re.search(r'Date:\s*(\S+)', text).group(1)
    features['total_amount'] = re.search(r'Total Amount:\s*\$?(\S+)', text).group(1)
    return features
