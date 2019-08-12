from listogram import Listogram

# split the corpus into sentences
import re

corpus = "This is a sentence. And this is also a sentence. One fish two fish and all that."

sentences = re.split(r' *[\.\?!][\'"\)\]]* *', corpus)
print(sentences)
bag_of_words = []
# make a dictogram of each sentence
for sentence in sentences:
    sentence = sentence.split(" ")
    # put them all into a list
    hist = Listogram(sentence)
    print(hist)
    bag_of_words.append(hist)

print(bag_of_words)