import random

word = random.choice(open('words2.txt','rt').read().split()).upper()

f = open('words.txt','rt')
worddump = f.read()
wordlist = worddump.split()
theWord = random.choise(wordlist)
theWord = theWord.upper()





print(word)

