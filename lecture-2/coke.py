def main():
   n = 50
   print("Amount Due: ", n)
   n = due(n)
   while n > 0:
       n = due(n)





def due(y):
    hell = int(input("Insert Coin: "))
    a = y - hell
    f = a * (-1)
    acc = [25, 10, 5]
    if a > 0 and hell not in acc:
        print("Amount Due:", y)
        return y
    elif a > 0 and hell in acc:
        print("Amount Due:", a)
        return a
    elif a <= 0:
        print("Change Owed:", f)


main()
