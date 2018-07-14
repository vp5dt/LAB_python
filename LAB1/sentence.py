print("program to find:\n1.Middle words\n2.Highest Length word\n3.Sentence in reverse order")

sentence=input("Enter sentence:")
def middle(sen):
    words=sen.split(" ")
    cenWord=[]
    center = int(len(words) / 2)

    if len(words)%2 ==0:
       cenWord.append(words[center-1])
       cenWord.append(words[center])
       # print(cenWord)
    else:
       cenWord=words[center]
    print("Middle words are:")
    print(cenWord)
def highestLength(sen):
    longWord=""
    words=sen.split(" ")
    for word in words:
        if(len(word)>len(longWord)):
            longWord=word
    print("Longest word is: ")
    print(longWord)
def reverse(sen):
    words=sen.split(" ")
    revSen=""
    for i in range(len(words)):
        for word in reversed(words[i]):
            revSen=revSen+word
        revSen=revSen+" "
    print("Sentence with reverse words is:")
    print(revSen)
middle(sentence)
highestLength(sentence)
reverse(sentence)

