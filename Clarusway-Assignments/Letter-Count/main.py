sentence=input("write a sentence\n")
result={word:sentence.count(word) for word in sentence}
print(result)
