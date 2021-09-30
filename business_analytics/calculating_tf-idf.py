import math
import pandas as pd

document_A = "the man went out for a walk"
document_B = "the children sat around the fire"

bag_Of_Words_A = document_A.split(" ")
bag_Of_Words_B = document_B.split(" ")

all_unique_words = set(bag_Of_Words_A).union(set(bag_Of_Words_B))
# print(all_unique_words)

num_of_word_A = dict.fromkeys(all_unique_words, 0)
for word_A in bag_Of_Words_A:
    num_of_word_A[word_A] += 1

num_of_word_B = dict.fromkeys(all_unique_words, 0)
for word_B in bag_Of_Words_B:
    num_of_word_B[word_B] += 1

# number of time word appeared / number of all the words

# Term Frequency


def calculate_term_Frequency(dictionary_of_words, bag_of_words):
    term_f = {}
    len_bag = len(bag_of_words)
    for word, count in dictionary_of_words.items():
        term_f[word] = count / float(len_bag)
    return term_f


tf_A = calculate_term_Frequency(num_of_word_A, bag_Of_Words_A)
tf_B = calculate_term_Frequency(num_of_word_B, bag_Of_Words_B)


# Inverse Document Frequency
def calculate_IDF(documents):
    doc_len = len(documents)
    idf = {}
    idf = dict.fromkeys(documents[0].keys(), 0);
    for word, val in idf.items():
        if (val > 0):
            idf[word] += 1
    for word, val in idf.items():
        idf[word] = math.log(doc_len / float((val) + 1));
    return idf


all_docs = [num_of_word_A, num_of_word_B];
idfs = calculate_IDF(all_docs)


def cal_TF_IDF(tfBag_of_words, idfs):
    tfidfs = {}
    for word, val in tfBag_of_words.items():
        tfidfs[word] = val * idfs[word]
    return tfidfs


tfidfA = cal_TF_IDF(tf_A, idfs)
tfidfB = cal_TF_IDF(tf_B, idfs)

df = pd.DataFrame([tfidfA, tfidfB])
pd.set_option('display.max_columns', 11)
print(df);
