from pipeline.pipeline_manager import pipeline
from pprint import pprint
# using pathlib to itterate path of each file in the folder
from pathlib import Path

#  root folder for .txt dataset
folder = Path("dataset/.txt_type")

# dictionary to track docs id
doc_id = 0
doc_table = {}

# inverted index to keep track of docs where the word is 
inverted_index = {}


for file_path in folder.iterdir():
    if file_path.is_file():
        # tokenizing the file
        tokens = pipeline(file_path).tokens()
        
        # assigning the docs id and track docs path 
        doc_id += 1

        doc_table[doc_id] = {
            "path": str(file_path)
        }

        # Inverse Indexing 
        # dic["term":set()]
        for term in tokens:
            if term not in inverted_index:
                inverted_index[term] = set()
            # insert the doc id to the term dictionary
            inverted_index[term].add(doc_id)
        # print(f'\n{file_path}: \n {tokens}\n')

# pprint(doc_table)

# pprint(inverted_index)

# implementing a basic lookup 
query = input("Enter Word to search: ")

if query in inverted_index:
    print("Found in doc:", inverted_index[query])
else:
    print("No result found")