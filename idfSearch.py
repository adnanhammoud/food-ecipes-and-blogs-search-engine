from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(use_idf=True, smooth_idf=False, sublinear_tf=False)
openConcatenated = open("concatenated.txt", 'r', errors="ignore")
X = vectorizer.fit(openConcatenated)

index = 1

while index <= 100:
    strRead = "food_" + str(index) + ".txt"
    openFood = open(strRead, 'r', errors="ignore")
    readFood = openFood.read()
    X_array = vectorizer.transform([readFood]).toarray()[0]
    food = ''.join(str(X_array.tolist()))
    strWrite = "food_" + str(index) + "idf.txt"
    idf_file = open(strWrite, "w")
    write_file = idf_file.write(food)
    index = index + 1

