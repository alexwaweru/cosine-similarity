import numpy as np
from collections import Counter

def cos_sim(a, b):
	"""Takes 2 vectors a, b and returns the cosine similarity according 
	to the definition of the dot product
	"""
	dot_product = np.dot(a, b)
	norm_a = np.linalg.norm(a)
	norm_b = np.linalg.norm(b)
	return dot_product / (norm_a * norm_b)


def pairwise_vectorized_trial():
    # How many teams participated in the first world cup?
    # Who holds the record for top scorer in a single World Cup?
    # How many teams participated in the first world cup who holds record for top soccer a single
    sentence_1 = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]) 
    sentence_2 = np.array([0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

    # Should I sell my car myself or trade it in?
    # How important is car maintenance?
    # Should I sell my car myself or trade it in how important is maintenance
    sentence_3 = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0])
    sentence_4 = np.array([0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1])

    # How much does AWS SAM cost to use
    # Which languages does AWS SAM support
    # How much does AWS SAM cost to use which languages does
    sentence_5 = np.array([1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0])
    sentence_6 = np.array([0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1])

    # We should expect sentence_m and sentence_h to be more similar
    print(cos_sim(sentence_1, sentence_2))
    print(cos_sim(sentence_3, sentence_4))
    print(cos_sim(sentence_5, sentence_6))


def vectorizer(a,b,c,d,e,f):
    sentence = a + b + c + d + e + f
    sentences = [a.split(" "), b.split(" "), c.split(" "), d.split(" "), e.split(" "), f.split(" ")]
    words = sentence.split(" ")
    template = list(set(words))
    final = [[], [], [], [], [], []]
    for i in range(0, len(sentences)):
        for j in range(0, len(template)):
            if template[j] in sentences[i]:
                final[i].append(1)
            else:
                final[i].append(0)
    return final[0], final[1], final[2], final[3], final[4], final[5]


def fully_vectorized_trial():
    a = "How many teams participated in the first world cup "
    b = "Who holds the record for top scorer in a single World Cup "
    c = "Should I sell my car myself or trade it in "
    d = "How important is car maintenance "
    e = "How much does AWS SAM cost to use "
    f = "Which languages does AWS SAM support "

    st1, st2, st3, st4, st5, st6 = vectorizer(a,b,c,d,e,f)

    sentences = [st1, st2, st3, st4, st5, st6]
    for i in range(0,6):
        print('\n')
        for j in range(0,6):
            ans = cos_sim(sentences[i], sentences[j])
            print('{0:.4f}'.format(ans), end='\t', flush=True)
    print('\n')

#pairwise_vectorized_trial()
fully_vectorized_trial()