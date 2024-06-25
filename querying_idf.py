import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fastapi import FastAPI

app = FastAPI()

def get_similarity_idf(query):
    index = 1
    vectorizer = TfidfVectorizer(use_idf=True, smooth_idf=False, sublinear_tf=False)
    openConcatenated = open("concatenated.txt", 'r', errors="ignore")
    X = vectorizer.fit(openConcatenated)
    X_array = vectorizer.transform([query]).toarray()[0]
    listQuery = X_array
    idfmap = {}
    while index <= 100:
        strRead = "food_" + str(index) + "idf.txt"
        openFood = open(strRead, 'r', errors="ignore")
        readFood = openFood.read()
        readFoodModified = readFood[1:-1]
        listFoodTemp = readFoodModified.split(", ")
        listFood = [float(element.replace("'", "")) for element in listFoodTemp]
        listFood = np.array(listFood)
        similarity = cosine_similarity([listQuery], [listFood])[0][0]
        index = index + 1
        idfmap[index] = similarity
        if index == 100:
            sorted_idf_map = dict(sorted(idfmap.items(), key=lambda item: item[1], reverse=True))

    return sorted_idf_map

def read_text_file(file_path):
    with open(file_path, 'r', errors="ignore") as file:
        return file.read()

@app.get("/similar_documents/{query}")
def get_similar_documents(query: str):
    similarity_map = get_similarity_idf(query)
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
