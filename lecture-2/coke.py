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
    if a > 0:
        print("Amount Due: ", a)
    elif a <= 0:
        print("Change Owed: ", f)
    return a



main()