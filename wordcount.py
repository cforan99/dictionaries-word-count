# put your code here.
""" Print a list of each word in a document and a count of how many times its used

    First we will iterate over each line in text file and each word in the line. 
    Then we will append the dictionary with the word if it is not in there. Once a new
    word is added, then we will keep count how many times it is used. Finally, we will
    end with a printed list of all unique words and how many times they were used in
    the text file.

"""
unique_words = {}

text_file = open("test.txt")

for line in text_file:
    line = line.rstrip()
    words = line.split(' ')
    
    for word in words:
        word = word.rstrip("?!.,")
        if word != "I":
            word = word.lower()
        if unique_words.get(word, 0) == 0:
            unique_words[word] = 1
        else: 
            unique_words[word] += 1 

print unique_words

