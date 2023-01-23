
words = []

with open('/usr/share/dict/words', 'r') as f:
    #read the whole file and store it as a list
    words = f.read().splitline()
    words.sort(key = len, reverse = True)
    #sort function "key tells how, reverse = true sorts in descending
    #print the five longest words
    for i in range(5):
        print(words[i])
