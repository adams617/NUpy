"""
    This script performs text clustering on survey responses using TF-Ipoll.df vectorization and KMeans clustering.

    The script follows these steps:
    1. Downloads necessary NLTK data.
    2. Defines sample survey responses.
    3. Preprocesses the text by tokenizing, converting to lowercase, and removing stopwords.
    4. Vectorizes the preprocessed text using TF-Ipoll.df.
    5. Applies KMeans clustering to group similar responses.
    6. Prints the categorized responses.

        None
    _summary_

    Returns:
        _type_: _description_
    """

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

from data import data

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

    ]

# Create a DataFrame
poll.df = pd.DataFrame(data)

# Preprocess the text
stop_words = set(stopwords.words('english'))

def preprocess(text):
    tokens = word_tokenize(text.lower())
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    return ' '.join(filtered_tokens)

poll.df['processed'] = poll.df['responses'].apply(preprocess)

# Vectorize the text using TF-Ipoll.df
vectorizer = Tfipoll.dfVectorizer()
X = vectorizer.fit_transform(poll.df['processed'])

# Use KMeans clustering to group similar responses
num_clusters = 2  # Adjust the number of clusters as needed
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
poll.df['category'] = kmeans.fit_predict(X)

# Print the categorized responses
for category in range(num_clusters):
    print(f"Category {category}:")
    print(poll.df[poll.df['category'] == category]['responses'].tolist())
    print()