from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from elasticsearch import Elasticsearch
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import json
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK resources
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Set up stopwords
stopWords = set(stopwords.words('english'))
stopWords.add(';')
stopWords.add('.')
stopWords.add(':')
stopWords.add(',')
stopWords.add('-')
stopWords.add('_')

# Create an instance of the FastAPI class
app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connect to Elasticsearch
es = Elasticsearch(
  "https://8bd56df5e20b46cc8ead6d3bb2c4c601.us-central1.gcp.cloud.es.io:443",
  basic_auth=['elastic', 'bAUJvxHezUKZnNpVrZzMK5Fq']
)

# Set up lemmatizer
lemmatizer = WordNetLemmatizer()

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
        similarity = cosine_similarity([listQuery], [listFood])[0][0]
        tfmap[index] = similarity
        index = index + 1

        if index == 100:
            sorted_tf_map = dict(sorted(tfmap.items(), key=lambda item: item[1], reverse=True))
    return sorted_tf_map

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

document_data = []
@app.get("/search")
async def search(query: str = None, searchOption: str = None):
    # Tokenize and filter stopwords
    foodTokenized = word_tokenize(query)
    foodStopwords = [word for word in foodTokenized if word not in stopWords]

    # Lemmatize the words
    processedQuery = " ".join(lemmatizer.lemmatize(word) for word in foodStopwords)

    # Perform a search query based on the selected search_option
    if searchOption == "default":
        response = es.search(index="search-foodrecipe", body={
            "query": {
                "match": {
                    "combined": processedQuery,
                }
            }
        })
    elif searchOption == "tf":
        responses = []
        similarity_map_tf = get_similarity_tf(query)

        for key in list(similarity_map_tf)[:15]:
            filename = f"food_{key}j.json"
            similarity = similarity_map_tf[key]
            updated_content = {'similarity': similarity}
            with open(filename, 'r', errors="ignore") as file:
                try:
                    existing_content = json.load(file)
                except json.JSONDecodeError:
                    existing_content = {}
            existing_content.update(updated_content)
            with open(filename, 'w') as file:
                json.dump(existing_content, file)
            with open(filename, 'r') as file:
                updated_content = json.load(file)
                responses.append(updated_content)
        return responses
    elif searchOption == "idf":
        responses = []
        similarity_map_idf = get_similarity_idf(query)

        for key in list(similarity_map_idf)[:15]:
            filename = f"food_{key}j.json"
            similarity = similarity_map_idf[key]
            updated_content = {'similarity': similarity}
            with open(filename, 'r', errors="ignore") as file:
                try:
                    existing_content = json.load(file)
                except json.JSONDecodeError:
                    existing_content = {}
            existing_content.update(updated_content)
            with open(filename, 'w') as file:
                json.dump(existing_content, file)
            with open(filename, 'r') as file:
                updated_content = json.load(file)
                responses.append(updated_content)
        return responses

    hits = response["hits"]["hits"]
    results = [{
        'title': hit['_source']['title'],
        'description': hit['_source']['description'],
        'nationality': hit['_source']['nationality'],
        'rating': hit['_source']['rating'],
        'time': hit['_source']['time'],
        'similarity': hit['_score'],
    } for hit in hits]

    return results