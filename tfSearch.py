
from sklearn.feature_extraction.text import CountVectorizer


vectorizer = CountVectorizer()
openConcatenated = open("concatenated.txt", 'r', errors="ignore")
X = vectorizer.fit(openConcatenated)

index = 1

while index <= 100:
    strRead = "food_" + str(index) + ".txt"
    openFood = open(strRead, 'r', errors="ignore")
    readFood = openFood.read()
    X_array = vectorizer.transform([readFood]).toarray()[0]
    food = ''.join(str(X_array.tolist()))
    strWrite = "food_" + str(index) + "tf.txt"
    tf_file = open(strWrite, "w")
    write_file = tf_file.write(food)
    index = index + 1

