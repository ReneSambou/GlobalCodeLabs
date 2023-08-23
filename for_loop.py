#for i in range(1,11):
#    print (i)

#for j in [1, 2, 3]:
#    print (j)

def star():
    i = "****"
    #a = len(i)
    for a in range(0,4):
        print(i)
    
star()

def grow(rows):
    i = "*"
    for a in range(1,rows):
        if a>rows/2:
            print((rows-a)*i)
        else:
            print( a*i)
grow(8)


def finder():
    string = input("Enter a word ")
    a = input("which letter do you want to find ")
    return string.count(a) > 0
print(finder())

def finder2():
    string = input("Enter a word ")
    string_set = set(string)
    a = input("which letter do you want to find ")
    return string_set.__contains__(a)
print(finder2())
    