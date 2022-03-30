def kitkatnodiv():
    threecount=0
    fivecount=0
    for i in range(1, 101):
        threecount+=1
        fivecount+=1

        if threecount == 3 and fivecount == 5:
            threecount=0
            fivecount=0
            print("KitKat")
        elif threecount == 3:
            threecount=0
            print("Kit")
        elif fivecount == 5:
            fivecount=0
            print("Kat")
        else:
            print(i)

def kitkat():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("KitKat")
        elif i % 3 == 0:
            print("Kit")
        elif i % 5 == 0:
            print("Kat")
        else:
            print(i)

def main():
    kitkat()
    kitkatnodiv()

if __name__ == "__main__":
    main()

