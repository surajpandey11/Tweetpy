import pandas as pd
import numpy as np
from nltk.stem.porter import *

import re
class TweetClean:
    def Clean_text(self,text):
        stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
                     "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
                     "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
                     "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had",
                     "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as",
                     "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through",
                     "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off",
                     "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how",
                     "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not",
                     "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should",
                     "now"]

        if text:
            text = ' '.join(text.split('.'))
            text = re.sub(r'\s+', ' ', re.sub('[^a-zA-Z#]', ' ', text.strip().lower())).strip()
            text = re.sub(r'\W+', ' ', text.strip().lower()).strip()
            text = [word for word in text.split()]
            text=[word for word in text if word not in stopwords]
            text=' '.join(text)
            return text
        return []


    def Standardize_text(self,text):
        stemmer = PorterStemmer()
        text = [word for word in text.split()]
        text=[stemmer.stem(word) for word in text ]
        text = ' '.join(text)
        return text



