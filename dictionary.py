test_dict={
    'Codingal':3,
    'is':2,
    'best':2,
    'for':2,
    'coding':1,
}
word=input("Enter the word you want to check th frequency of:")
frequency=test_dict.get(word,0)
print("The frequency of",word,"is:",frequency)