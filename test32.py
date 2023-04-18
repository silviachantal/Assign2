def query_convertorbigr(querywd):
    size = len(querywd)
    # we add the end of string symbol "$" to the query word 
    querywd = querywd + "$"
    # we find where the index of the kleene star is 
    index = querywd.find("*")
    # we transform the query word in the shape of what originally comes after the kleene start 
    # + what originally comes before, followed by the start itself (end of string)
    querywd = querywd[index+1:size+1] + querywd[0:index]
    for i in range(len(querywd)-1):
        querywd = querywd[i:i+2]

    return querywd