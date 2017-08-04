a = "soccer"
b = "gamer"
c = "magician"
myAnswer = input("pick 1 'a' = soccer ,'b' = gamer,'c' magician")

while myAnswer != a and myAnswer != b and myAnswer != c:
    if myAnswer == "a":
        print ("soccer was Chosen Good job")

    elif myAnswer == "b":
        print ("gamer was chosen Good job!")

    elif myAnswer == "c":
        print ("magician")
    else:
        myAnswer = input("pick 1 'a' = soccer ,'b' = gamer,'c' magician")
