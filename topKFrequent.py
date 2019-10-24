from .maxHeap import MaxHeap

class Solution:
    def topKFrequent(self, words, k):
        #word : occurances
        wordOccurances = {}

        for word in words:
            if wordOccurances.get[word]:
                #add to the count
                wordOccurances[word] += 1
            else:
                #create the key with the count value
                wordOccurances[word] = 1

        #creates a maxheap of the occurances of each word
        occuranceHeap = MaxHeap(list(wordOccurances.values()))

        #new dictionary where key and values are flipped
        occuranceWords = {}

        for key, value in wordOccurances.items():
            #check if the value is already a key in the new dictionary
            if value in occuranceWords:
                #append the key as a value into the list
                occuranceWords[value].append(key)
            else:
                #create a key with the value and append value as a list containing just the key
                occuranceWords[value] = [key]
        
        frequentWords = []
        pops = k
        while pops > 0:
            #get max frequency
            freq = occuranceHeap.pop()
            #check if key exists
            if occuranceWords.get(freq):
                #append the list of words with that frequency to our final list; keep alphabetical order using sorted()
                frequentWords += sorted(occuranceWords[freq])
                #increment pops by the number of words we added to the list
                pops -= len(occuranceWords[freq])
                #remove the key so we avoid duplications in results
                del occuranceWords[freq]

        #get top k elements
        frequentWords = frequentWords[:k]
        return frequentWords



