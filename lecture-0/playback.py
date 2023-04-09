def main():
    elipsis()


#Defining function that replaces all spaces with 3 elipses
def elipsis():
    name = str(input("Enter your sentence here: ")).replace(" ", "...")
    print(name)
main()