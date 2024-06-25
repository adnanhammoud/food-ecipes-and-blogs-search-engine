# 3- Pre-processing the text files (stemming, tokenization, stop-word removal
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

index = 1
while index <= 100:
    strRead = "food_" + str(index) + ".txt"
    openFood = open(strRead, 'r', encoding="utf-8")
    readFood = openFood.read()
    foodTokenized = word_tokenize(readFood)
    foodStopwords = []
    for word in foodTokenized:
        if word not in stopWords:
            foodStopwords.append(word)
    lemmatizer = WordNetLemmatizer()
    #stemmer = PorterStemmer()
    food = ""
    for word in foodStopwords:
        food = food + lemmatizer.lemmatize(word) + " "

    strWrite = "food_" + str(index) + "pp.txt"
    writeFood = open(strWrite, 'w')
    writeFood.write(food)
    index = index + 1
    closeFood = openFood.close()
