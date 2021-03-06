import sys
import filecmp

# c)
def compare_op():
    original_stdout = sys.stdout # Save the original standard output

    with open('kitkat.txt', 'w') as f:
        sys.stdout = f # Change the standard output to file kitkat.txt
        kitkat()
        f.close()
    with open('kitkatnodiv.txt', 'w') as f:
        sys.stdout = f # Change the standard output to file kitkatnodiv.txt
        kitkatnodiv()
        f.close()
    sys.stdout = original_stdout # Restore standard output

    files_equal=filecmp.cmp('kitkat.txt', 'kitkatnodiv.txt')
    print(files_equal)

# b)
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

# a)
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
#    kitkat()
#    kitkatnodiv()
    compare_op()

if __name__ == "__main__":
    main()

