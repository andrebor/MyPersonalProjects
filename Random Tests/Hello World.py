def helloWorld(myString):
    print(myString)
    MyName = input("What is your name?")
    MyVar = input("Enter a number")

    if (MyName == "André" or MyVar == 0):
        print("André is Great!")
    elif (MyName == "Bob"):
        print("Bob is ok")
    else:
        print("Hello World!")

helloWorld("roflcompter")