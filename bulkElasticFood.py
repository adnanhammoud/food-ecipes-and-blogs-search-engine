# 6- Bulking the documents into elastic search (write once only) and testing the results
from elasticsearch import Elasticsearch
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

stopWords = set(stopwords.words('english'))
stopWords.add(';')
stopWords.add('.')
stopWords.add(':')
stopWords.add(',')
stopWords.add('-')
stopWords.add('_')

client = Elasticsearch(
  "https://8bd56df5e20b46cc8ead6d3bb2c4c601.us-central1.gcp.cloud.es.io:443",
  basic_auth=['elastic', 'bAUJvxHezUKZnNpVrZzMK5Fq']
)
print(client.info())

documents = open("elasticFood.json", 'r')
with open('elasticFood.json', 'r') as file:
  documents = file.read()

# print(client.bulk(index= 'search-foodrecipe', operations=documents.split('\n'), pipeline="ent-search-generic-ingestion", refresh=True))

query = "Vanilla cake with sprinkles"
foodTokenized = word_tokenize(query)
foodStopwords = []
for word in foodTokenized:
    if word not in stopWords:
        foodStopwords.append(word)
lemmatizer = WordNetLemmatizer()
    # stemmer = PorterStemmer()
processedQuery = ""
for word in foodStopwords:
    processedQuery = processedQuery + lemmatizer.lemmatize(word) + " "

print(client.search(index="search-foodrecipe", body={
            "query": {
                "match": {
                    "combined": processedQuery
                }
            }
        }))