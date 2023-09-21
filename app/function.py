import os
from flask import current_app as app
from flask import  flash,redirect
from .models import List
from . import db
from os import path
from sqlalchemy import text 
import pandas as pd


def addlist(file_path):
    if os.path.exists(file_path):
        _, file_extension = os.path.splitext(file_path)

        if file_extension.lower() == '.xlsx' or file_extension.lower() == '.xls':
            sheet_names = pd.ExcelFile(file_path).sheet_names
        elif file_extension.lower() == '.csv':
            sheet_names = [None]  # For CSV, we don't need sheet names
        else:
            return print("Unsupported file format")

        data_to_insert = []

        for sheet_name in sheet_names:
            if file_extension.lower() == '.xlsx' or file_extension.lower() == '.xls':
                if sheet_name:
                    df = pd.read_excel(file_path, sheet_name, engine='openpyxl')
                else:
                    df = pd.read_excel(file_path, engine='openpyxl')
            elif file_extension.lower() == '.csv':
                df = pd.read_csv(file_path)
            else:
                return print("Unsupported file format")

            for index, row in df.iterrows():
                # Assuming 'list' is a column name in your Excel/CSV file
                list_name = row.get('list')

                # Check if a List entry with the same name already exists
                existing_list = db.session.query(List).filter_by(url=list_name).first()
                prdata=[]
                prdata.append(list_name)

                if not existing_list:
                    data_to_insert.append({
                        'url': list_name
                    })
                else:
                    print(f"List with name '{list_name}' already exists in the database.")
        print(prdata)
        if data_to_insert:
            db.session.bulk_insert_mappings(List, data_to_insert)
            db.session.commit()
            
            print("Data added successfully.")
        else:
            print("No new data to add.")
    else:
        print("File not found")

import re
from collections import Counter
import math

# Tokenize a text into words
def tokenize(text):
    text = text.lower()
    tokens = re.findall(r'\w+', text)
    return [word for word in tokens if len(word) > 0]

# Calculate cosine similarity between two tokenized texts
def cosine_similarity(text1, text2):
    tokens1 = tokenize(text1)
    tokens2 = tokenize(text2)

    # Create Counter objects to count word frequencies
    word_count1 = Counter(tokens1)
    word_count2 = Counter(tokens2)

    # Calculate the dot product of the token vectors
    dot_product = sum(word_count1[word] * word_count2[word] for word in set(tokens1) & set(tokens2))

    # Calculate the magnitude (Euclidean norm) of the token vectors
    magnitude1 = math.sqrt(sum(word_count1[word] ** 2 for word in tokens1))
    magnitude2 = math.sqrt(sum(word_count2[word] ** 2 for word in tokens2))

    # Calculate the cosine similarity
    similarity = dot_product / (magnitude1 * magnitude2)

    return similarity


# text1 = "This is a sample text for testing."
# text2 = "This is a sample text for testing."

# similarity = cosine_similarity(text1, text2)
# print(f"Cosine Similarity: {similarity}")
