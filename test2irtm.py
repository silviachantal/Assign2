from collections import defaultdict
from typing import *

def permutator(vocab):
    #we create a dictionary to store terms of vocabulary as keys and their permutations as values
    permutations = defaultdict(list)
    #we iterate over each term in our vocabulary
    for term in vocab:
        #we make sure to exclude punctuations and numbers --> maybe change?
        if term.isalpha() == True:
            #in case the term is one letter or multiple same letters we do not need permutations
            if len(term) == 1 or term == term[0] * len(term):
                permutations[term].append(term)
            #in all other cases we first add the end of string symbol $ to then perform permutations
            else:
                termdollar = term + "$"
                
                #now we iterate over each character in each term 
                for char in range(len(termdollar)):
                    #and we store iteratively the first char followed by next in the term -1
                    allpermuts = termdollar[char:] + termdollar[:char]
                    #we append to our dictionary all the permutations of a specific term (key) as list (value)
                    permutations[term].append(allpermuts)
                
    return permutations     
def query_convertor(querywd):
    size = len(querywd)
    # we add the end of string symbol "$" to the query word 
    querywd = querywd + "$"
    # we find where the index of the kleene star is 
    index = querywd.find("*")
    # we transform the query word in the shape of what originally comes after the kleene start 
    # + what originally comes before, followed by the start itself (end of string)
    # remove start as well
    querywd = querywd[index+1:size+1] + querywd[0:index]
    return querywd

def queryvocabmatcher(queryword):
    # we get the lists of permutations of each term
    queryword = query_convertor(queryword)
    sizeqw = len(queryword)

    vocabu = permutator(['cacca'])
    # vocabu = {'cacca': ['cacca$', 'a$cacc', 'ca$cac', 'cca$ca', 'acca$c']}
    starindex = queryword.find('*')
    matches = []

    for key, val in vocabu.items():
    # we access each element of the list of permutations
        for word in val:
            if val.startswith(queryword):
                matches.append(key)
                break
        
        match = ""
        # we only want to make sure that the two strings match before the kleene star of query word and 
        # we want to find at what index in each query string the kleene star is to get end of match
        for item in val:
            if queryword[0] == "$":
                queryword = queryword[1:sizeqw]
            else:
                queryword = queryword[0:sizeqw]    
                for char, charct in zip(item, queryword):
                    if char == charct [:starindex]:
                        match = vocabu.keys()

                    matches.append(match)
    return matches


class TreeNode():
    def __init__(self) -> None:
        self.children : Dict[str, TreeNode] = defaultdict(TreeNode)
        self.terms = []

    @staticmethod 
    def construct_from_vocab( words: List[str]): # -> TreeNode:
        root = TreeNode()
        permuated_dict = permutator(words)
        for term, permuations in permuated_dict.items():
            for permutation in permuations:
                root.insert(permutation, term)
        return root

    def insert(self, permutation: str, term: str):
        if len(permutation) == 0:
            self.terms.append(term)
        else:
            # dog$
            ch = permutation[0] # d
            tail = permutation[1:] # og$
            child = self.children[ch]
            child.insert(tail,term)
    
    def query(self, query:str):
        query = query_convertor(query)
        return self.find_node_with_prefix(query)
    
    def find_node_with_prefix(self, query: str): # $do
        if len(query) == 0:
            return self.collect_match()
        else:
            ch = query[0] # d
            tail = query[1:] # og$
            child = self.children[ch] # FIXME this is bad with defaultdict
            return child.find_node_with_prefix(tail)
    
    def collect_match(self):
        result = []
        result += self.terms
        for child in self.children.values():
            result += child.collect_match()
        return result


tree = TreeNode.construct_from_vocab([)
print(tree.query("ti*"))

#def create_tree_iteratively(words : List[str]):
#    root = TreeNode()
#    permuated_dict = permutator(words)
#    for term, permuations in permuated_dict.items():
#        for permutation in permuations:
#            cur_node = root
#            for ch in permutation:
#                cur_node = cur_node.children[ch]
#            cur_node.terms.append(term)
#    return root
