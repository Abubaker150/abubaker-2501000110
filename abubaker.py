# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BT-GXIR63FRQGdiaB6jHjRpCTOou_n7n
"""

#Calculate Jaccard similarity

similarity = len(intersection) / len(union)

#Return similarity and intersecting words

return similarity, intersection

# Input texts

text1 = "This is a sample sample text about is this legal sample issues."

text2 = "This text legal discusses legal and ethical This issues in legal computir."

#Calculate similarity and get common words

similarity, common_words = jaccard_similarity(text1, text2)

a Print results 0.29

print(f"Similarity: (similarity:.2f}")
print9f"Common words: {common_words}")

#Calculate Jaccard similarity

similarity = len(intersection) / len(union)

#Return similarity and intersecting words

return similarity, intersection

# Input texts

text1 = "This is a sample sample text about is this legal sample issues."

text2 = "This text legal discusses legal and ethical This issues in legal computir."

#Calculate similarity and get common words

similarity, common_words = jaccard_similarity(text1, text2)

# Print results

print(f"Similarity: (similarity:.2f}")
print(f"Common words: {common_words}")

def jaccard_similarity(text1, text2):
    # Split texts into sets of words
    set1 = set(text1.split())
    set2 = set(text2.split())

    # Find intersection and union
    intersection = set1.intersection(set2)
    union = set1.union(set2)

    # Calculate Jaccard similarity
    similarity = len(intersection) / len(union)

    # Return similarity score and intersection (common words)
    return similarity, intersection

# Input texts
text1 = "This is a sample sample text about is this legal sample issues."
text2 = "This text legal discusses legal and ethical This issues in legal computing."

# Calculate similarity and get common words
similarity, common_words = jaccard_similarity(text1, text2)

# Print result
print(f"Similarity: {similarity:.2f}")
print(f"Common words: {common_words}")