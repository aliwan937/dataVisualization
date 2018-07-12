import json
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from textblob import TextBlob
from os import path
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
polarity  = []
subjectivity = []
combined = ""
filteredWords = {}

for i in range(len(tweetData)):
    text = TextBlob(tweetData[i]["text"])
    polarity.append(text.sentiment.polarity)
    subjectivity.append(text.sentiment.subjectivity)
    for word in text.words:
        if (len(word) >= 3 and word.isalpha()):
            combined += word
            if word in filteredWords:
                filteredWords[word] += 1
            else:
                filteredWords[word] = 1



for i in filteredWords:
    print("key:", i, "value:", filteredWords[i])

wordcloud = WordCloud().generate_from_frequencies(filteredWords)

plt.imshow(wordcloud,interpolation = 'bilinear')
plt.axis("off")
wordcloud = WordCloud(max_font_size=40).generate_from_frequencies(filteredWords)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

polaritySum = 0
for i in polarity:
    polaritySum += i
print("polarity average", polaritySum/len(polarity))

subjectivitySum = 0
for i in subjectivity:
    subjectivitySum += i
print("subjectivity average", subjectivitySum/len(subjectivity))

n, bins, patches = plt.hist(polarity, bins=[-1,-0.5,0.5,1],  bottom=None, histtype='bar', align='mid', orientation='vertical')
plt.grid(True)
plt.show()
