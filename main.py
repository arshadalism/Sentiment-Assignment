import pandas as pd
import string
from textblob import TextBlob
import matplotlib.pyplot as plt
import ftfy

df = pd.read_excel('user_review.xls')
df = df.dropna()
df = df[['review']]

df['review'] = df['review'].apply(ftfy.fix_text)


df['review'] = df['review'].str.lower()
df['review'] = df['review'].str.replace('[{}]'.format(string.punctuation), '', regex=True)
df['review'] = df['review'].str.replace('â€™', '')


def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'


df['sentiment'] = df['review'].apply(get_sentiment)
sentiment_counts = df['sentiment'].value_counts()

sentiment_counts.plot(kind='bar')

print(sentiment_counts)


plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.xticks(rotation=0)

plt.ylabel('Count')


plt.show()
