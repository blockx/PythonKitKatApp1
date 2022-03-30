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

if __name__ == "__main__":
    main()

