from collections import defaultdict
import nltk

def bigramidx(vocab):
    #we create a dictionary to store terms of vocabulary as keys and the bigrams as values
    bigrams = defaultdict(list)
    #we iterate over each term in our vocabulary
    for term in vocab:
        #we make sure to exclude punctuations and numbers --> maybe change?
        if term.isalpha() == True:
            termdollar = "$" + term + "$"
            termsbigrs = nltk.bigrams(termdollar)
            bigrams[term].append(termsbigrs)
                                               
    return bigrams

myvoc = ["park", "house", "dog"]
bigramidx(myvoc)


# def queryvocabmatcher(queryword):
# # we get the lists of permutations of each term
#     queryword = query_convertor(queryword)
#     vocabu = 
#     starindex = queryword.find('*')
#     matches = []

#     for val in testone.values():
#     # we access each element of the list of permutations
    
#         # we only want to make sure that the two strings match before the kleene star of query word and 
#         # we want to find at what index in each query string the kleene star is to get end of match
        
#         for item in val:
#             if queryword[0] == "$":
#                 match = item.startswith(queryword, 1, starindex)
#                 matches.append(match)
#             elif queryword[0].isalpha():
#                 match = item.startswith(queryword, 0, starindex)
#                 matches.append(match)
    
#     return matches
#     # WRONG: charmatch = item.split('*')[0]


# def query_convertor(querywd):
#     size = len(querywd)
#     # we add the end of string symbol "$" to the query word 
#     querywd = querywd + "$"
#     # we find where the index of the kleene star is 
#     index = querywd.find("*")
#     # we transform the query word in the shape of what originally comes after the kleene start 
#     # + what originally comes before, followed by the start itself (end of string)
#     querywd = querywd[index+1:size+1] + querywd[0:index+1]
#     return querywd


# def permutator(vocab):
#     #we create a dictionary to store terms of vocabulary as keys and their permutations as values
#     permutations = defaultdict(list)
#     #we iterate over each term in our vocabulary
#     for term in vocab:
#         #we make sure to exclude punctuations and numbers --> maybe change?
#         if term.isalpha() == True:
#             #in case the term is one letter or multiple same letters we do not need permutations
#             if len(term) == 1 or term == term[0] * len(term):
#                 permutations[term].append(term)
#             #in all other cases we first add the end of string symbol $ to then perform permutations
#             else:
#                 term = term + "$"
#                 #now we iterate over each character in each term 
#                 for char in range(len(term)):
#                     #and we store iteratively the first char followed by next in the term -1
#                     allpermuts = term[char:] + term[:char]
#                     #we append to our dictionary all the permutations of a specific term (key) as list (value)
#                     permutations[term].append(allpermuts)
                
#     return permutations 