str = open('paragraph_1.txt', 'r').read()
words = str.split(' ')
num_of_words = len(words)
print ("Words:", num_of_words)
sentences = str.split ('.')
num_of_sentences = len(sentences)
print ("Sentences:",num_of_sentences)

letters = str
num_of_letters = len(letters) 
print ("Letters:", num_of_letters)

averageLetter = num_of_letters/num_of_words
print ("Average Letters: ", averageLetter)

averageSentence = num_of_words/num_of_sentences
print ("Average Sentence Length:",averageSentence)
print (str)