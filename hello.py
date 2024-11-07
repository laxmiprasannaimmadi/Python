import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
lemma = WordNetLemmatizer()

text = "Python has different libraries such as pandas, numpy, pytorch, scikit-learn, etc"
x = re.sub('[^a-zA-Z]',' ',text ).split()
x = [lemma.lemmatize(word) for word in x if word not in set(stopwords.words("english"))]
x = " ".join(x)
print(x)