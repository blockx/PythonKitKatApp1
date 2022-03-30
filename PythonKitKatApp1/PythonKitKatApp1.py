def kitkat(max):
    if (max != 0):
        for i in range(1, 100, 1):
            found_kit = False
            found_kat = False

            if ((i % 3) == 0): 
                found_kit = True;
            if ((i % 5) == 0): 
                found_kat = True;

            if found_kit == True and found_kat == True:
                print("KitKat")
            elif found_kit == True:
                print("Kit")
            elif found_kat == True:
                print("Kat")
            else:
                print(i)



def main():
    kitkat(100)

if __name__ == "__main__":
    main()

