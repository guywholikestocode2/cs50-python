def main():
    interpret()


def interpret():
    L = input("Please enter operation to be performed: ")
    x, y, z = L.split(" ")
    x = int(x)
    z = int(z)
    if y == "/":
        print(float(x/z))
    if y == "+":
        print(float(x + z))
    if y == "-":
        print(float(x - z))
    if y == "*":
        print(float(x * z))
main ()
