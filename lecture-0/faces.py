def main():
    convert()


#Defining function to convert emoticons to emojis
def convert():
    name = input(" ").replace(":)", "🙂").replace(":(", "🙁")
    print(name)


main()
