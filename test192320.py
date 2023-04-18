from collections import defaultdict 

def bigramidx(vocab):
    #we create a dictionary to store terms of vocabulary as keys and the bigrams as values
    bigrams = defaultdict(list)
    #we iterate over each term in our vocabulary
    for term in vocab:
        #we make sure to exclude punctuations and numbers 
        if term.isalpha() == True:
            termdollar = "$" + term + "$"
            for i in range(len(termdollar)-1):
                termbigrs = termdollar[i:i+2]
                #termsbigrs = nltk.ngrams(termdollar, 2) #nltk version
                bigrams[term].append(termbigrs)
                                               
    return bigrams

# this changes from the permut convertor because before returning 
# we split into bigrams 
def query_convertorbigr(querywd):
    size = len(querywd)
    # we add the end of string symbol "$" to the query word 
    querywd = querywd + "$"
    # we find where the index of the kleene star is 
    index = querywd.find("*")
    # we transform the query word in the shape of what originally comes after the kleene start 
    # + what originally comes before, followed by the start itself (end of string)
    querywd = querywd[index+1:size+1] + querywd[0:index]
    bigrqueryres = ""
    for i in range(len(querywd)-1):
        bigrqueryres = bigrqueryres + " " + querywd[i:i+2]
        

    return bigrqueryres





class TreeNode():
    def __init__(self) -> None:
        self.children : Dict[str, TreeNode] = defaultdict(TreeNode)
        self.terms = []

    @staticmethod 
    def construct_from_bigramidx( words: List[str]): # -> TreeNode:
        # we initialize our Tree object by setting the root node
        root = TreeNode()
        # we create all the permutations
        bigrm_dict = bigramidx(words)
        for term, bigrams in bigrm_dict.items():
            # we add a bigram to a new root 
            for bigram in bigrams:
                root.insert(bigram, term)
        return root

    def insert(self, bigram: str, term: str):
        
        # each time we reach the end of the bigrams we add the final matching term
        # to the list of all terms matching
        if len(bigram) == 0:
            self.terms.append(term)
        else:
            ch = bigram[0] 
            tail = bigram[1:] 
            child = self.children[ch]
            child.insert(tail,term)
    
    def querybigram(self, query:str):
        query = query_convertorbigr(query)
        
        for bigram in query:
            self.terms.append(self.find_node_with_prefix(bigram))
        #return self.find_node_with_prefix(query)  
        for i in self.terms:
            a = i.children
            for u in a:
                print(u.keys())
        return self.terms
    
    def find_node_with_prefix(self, query: str): # do
        if len(query) == 0:
            return self.collect_match()
        else:
            ch = query[0] # d
            tail = query[1:] # o
            child = self.children[ch].children[tail]
            while(len(child.children) != 0):
                child = child.children
            return child
    
    def collect_match(self):
        result = []
        result += self.terms
        for child in self.children.values():
            result += child.collect_match()
        return result