def query_convertor(querywd):
    size = len(querywd)
    # we add the end of string symbol "$" to the query word 
    querywd = querywd + "$"
    # we iterate over the character of the word in the query
    for charac in range(size):
        #we rotate until we get the kleene star at the end 
        if querywd[size -1] == "*":
            querypermut = querywd[charac:] + querywd[:charac]
        return querypermut

print(query_convertor("ze*st"))