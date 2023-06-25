def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    valid = True
    if len(s) < 2 or len(s) > 6:
        valid = False
    punct = [" ", ".", ",", ":", ";", "!", "?", "/", "-", "_"]
    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] #have to fix the int problem
    A = len(s)
    inthell = ""
    for i in s:
        if i in num:
            inthell += i

    strhell = ""
    for i in s:
        if i.isalpha():
            strhell += i
        else:
            strhell += " "

    strhell1 = strhell[::-1]

    for i in strhell1:
        if i == " ":
            strhell1 = strhell1.replace(i, "", 1)
        elif i.isalpha():
            break

    strhell = strhell1[::-1]

    for i in s:
        if i in punct:
            valid = False

    if inthell == "":
        valid = valid
    elif inthell[0] == "0":
        valid = False


    for i in strhell:
        if i == " ":
            valid = False
            print(i)
        else:
            continue
    return valid



main()