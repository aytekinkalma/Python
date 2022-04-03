def missing_char(word, n):
    result=''
    counter=0
    for i in word:
        result+=i
        if counter==n:
            result=result.strip(i)
        
        counter+=1
        
            
    return result
