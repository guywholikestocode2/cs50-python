def main():
    twttr = input("Input: ")
    vowel(twttr)




def vowel(x):
    vowel_string = ""
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for i in x:
        if i not in vowels:
            vowel_string += i
        elif i in vowels:
            pass
    print("Output:", vowel_string)



main()