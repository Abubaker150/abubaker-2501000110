# -*- coding: utf-8 -*-
"""cood

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HXxjc-HrtWLRWn9CGeW6qDYRNqQNzN2a
"""

import pandas as pd

def jaccard_similarity(text1, text2):
    # Split texts into sets of words
    set1 = set(text1.split())
    set2 = set(text2.split())

    # Calculate intersection and union
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))

    # Calculate Jaccard similarity
    similarity = intersection / union if union else 0  # Avoid division by zero

    # Find common words
    common_words = list(set1.intersection(set2))

    return similarity, common_words

# Define phishing keywords
phishing_keywords = ["urgent", "password reset", "bank", "verify", "account suspended"]
#These are words commonly found in phishing emails.
#The script will check if an email contains any of these words.

# Load the dataset (uploaded file)
emails = pd.read_csv("/content/2501000110.csv")

# Check if the 'content' column exists
if 'content' in emails.columns:
    # Apply phishing detection
    emails["is_phishing"] = emails["content"].apply(
        lambda x: any(keyword in str(x).lower() for keyword in phishing_keywords)
    )


    # Save the processed file
    emails.to_csv("/content/analyzed_emails.csv", index=False)
import pandas as pd

def jaccard_similarity(text1, text2):
    # Split texts into sets of words
    set1 = set(text1.split())
    set2 = set(text2.split())

    # Calculate intersection and union
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))

    # Calculate Jaccard similarity
    similarity = intersection / union if union else 0  # Avoid division by zero

    # Find common words
    common_words = list(set1.intersection(set2))

    return similarity, common_words

# Define phishing keywords
phishing_keywords = ["urgent", "password reset", "bank", "verify", "account suspended"]
#These are words commonly found in phishing emails.
#The script will check if an email contains any of these words.

# Load the dataset (uploaded file)
emails = pd.read_csv("/content/2501000110.csv")

# Check if the 'content' column exists
if 'content' in emails.columns:
    # Apply phishing detection
    emails["is_phishing"] = emails["content"].apply(
        lambda x: any(keyword in str(x).lower() for keyword in phishing_keywords)
    )


    # Save the processed file
    emails.to_csv("/content/analyzed_emails.csv", index=False)
    print("Phishing detection complete. ✅")
else:
    print("Error")

from google.colab import drive
drive.mount('/content/drive')