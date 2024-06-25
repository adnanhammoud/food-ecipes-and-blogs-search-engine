import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fastapi import FastAPI
import json

app = FastAPI()

def get_similarity_tf(query):
    index = 1
    vectorizer = CountVectorizer()
    openConcatenated = open("concatenated.txt", 'r', errors="ignore")
    X = vectorizer.fit(openConcatenated)
    X_array = vectorizer.transform([query]).toarray()[0]
    listQuery = X_array
    tfmap = {}
    while index <= 100:
        strRead = "food_" + str(index) + "tf.txt"
        openFood = open(strRead, 'r', errors="ignore")
        readFood = openFood.read()
        readFoodModified = readFood[1:-1]
        listFoodTemp = readFoodModified.split(", ")
        listFood = [int(element.replace("'", "")) for element in listFoodTemp]
        listFood = np.array(listFood)
        # print(len(listFood))
        similarity = cosine_similarity([listQuery], [listFood])[0][0]
        tfmap[index] = similarity
        index = index + 1

        if index == 100:
            sorted_tf_map = dict(sorted(tfmap.items(), key=lambda item: item[1], reverse=True))

    return sorted_tf_map

def read_text_file(file_path):
    with open(file_path, 'r', errors="ignore") as file:
        return file.read()

@app.get("/similar_documents/{query}")
def get_similar_documents(query: str):
    similarity_map = get_similarity_tf(query)
    document_data = []

    for key in list(similarity_map)[:15]:
        file_path = f"food_{key}j.json"
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                document_data.append({
                    "title": data.get("title", ""),
                    "description": data.get("description", ""),
                    "rating": data.get("rating", ""),
                    "time": data.get("time", ""),
                    "nationality": data.get("nationality", "")
                })
        except FileNotFoundError:
            # Handle missing files
            pass

    return document_data
