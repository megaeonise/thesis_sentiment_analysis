# import libraries
import pandas as pd

import nltk

from nltk.sentiment.vader import SentimentIntensityAnalyzer

from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize

from nltk.stem import WordNetLemmatizer

from sklearn.metrics import confusion_matrix


# download nltk corpus (first time only)


# Load the amazon review dataset

analyzer = SentimentIntensityAnalyzer()


# def preprocess_text(text):
#     tokens = word_tokenize(text.lower())

#     filtered_tokens = [
#         token for token in tokens if token not in stopwords.words("english")
#     ]

#     lemmatizer = WordNetLemmatizer()

#     lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

#     processed_text = " ".join(lemmatized_tokens)
#     return processed_text


# def get_sentiment(text):

#     scores = analyzer.polarity_scores(text)
#     sentiment = 1 if scores["pos"] > 0 else 0
#     return sentiment


# df = pd.read_csv(
#     "https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/amazon.csv"
# )

# print(df)

# df["reviewText"] = df["reviewText"].apply(preprocess_text)
# df["sentiment"] = df["reviewText"].apply(get_sentiment)

# print(df, "lemmatized and sentimentized")
# print(confusion_matrix(df["Positive"], df["sentiment"]))
