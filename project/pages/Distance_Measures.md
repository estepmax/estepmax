title: Distance Measures
date: 2018-03-05
abstract: Some interesting distance measures and their everyday uses.
topic: Information Retrieval
color: "F0433A"
unlisted: 0

##Cosine Similarity		
This measure in particular is based off of the Euclidian dot product which calculates the angle between two vectors: $$cos(\theta)=\dfrac{A\cdot{B}}{\|A \| \|B\|} \Leftrightarrow \dfrac{\sum_{i=1}^n A_{i}B_{i}}{\sqrt{\sum_{i=1}^n A_{i}}\sqrt{\sum_{i=1}^n B_{i}}}$$ 

Suppose we are given the two following sentences: <b> The dog jumps over the high fence </b> and  <b> The cat runs to the fence </b>. Now, we want to figure out the similarity between these two sentences. One slight change we need to make in order
to use the cosine similarity measure for strings is to create "word vectors" out of the words in our corpus of text. 
``` python
A = 'The dog jumps over the fence'.lower()
B = 'The cat runs up to the fence'.lower()

A,B = A.split(),B.split() #split sentences into word vectors

word_basis = list(set(A) | set(B)) #get union of both word vectors

#get word count from each sentence and downcast into a dictionary
A_freq = [{A[i]:A.count(A[i]) for i in range(0,len(A))}][0] 
B_freq = [{B[j]:B.count(B[j]) for j in range(0,len(B))}][0]
word_freq = [A_freq,B_freq]

corpus_dict = dict() #corpus dictionary
freq_collection = [] #temporary location 


#this section of code is used to create a corpus dictionary based on 
#a collection of sentences

for k in range(0,len(word_basis)):
    key = word_basis[k]
    for l in range(0,len(word_freq)):
        if key in word_freq[l].keys():
            freq_collection.append(word_freq[l][key])
        else:
            freq_collection.append(0)
        corpus_dict[key] = freq_collection
    freq_collection = [] #clear each pass
            
```

The above code is just preprocessing, now onto calculating a value.

```python
import numpy as np
from __future__ import division #for decimal precision

K = np.array(corpus_dict.values()) #recasting as a numpy array 

dot_product = np.dot(K[:,0],K[:,1]) #dot product of both counts
sum_A = np.sum(K[:,0]**2) #sum of squares for sentence A
sum_B = np.sum(K[:,1]**2) #sum of squares for sentence B

cos_similarity = dot_product/(np.sqrt(sum_A)*np.sqrt(sum_B)) 

cos_similarity	#0.58925565098878951
```

##Jaccard Similarity

The Jaccard similarity comes from a set theory point of view which takes on the following form: $$ J(A,B) = \dfrac{|A \cap B|}{|A \cup B|}$$
 
```python
word_basis_int = list(set(A) & set(B)) #intersection of word vectors
jaccard_dist = len(word_basis_int)/len(word_basis)
jaccard_dist #0.22222222
```

Note that stop words are not taken into consideration in either example, you should take care of them in practice.
There are plenty of distance measures available to use other than the ones I have implemented - it is up to you 
to play with and discover. 

<b>-M<b>