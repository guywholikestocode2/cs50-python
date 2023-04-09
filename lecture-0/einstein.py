def main():
    mass = int(input("Enter the mass in integer form: ")) #Asking the user to input the mass value in integer form
    einstein(mass)



#Defining function to calculate energy when mass is given
def einstein(to):
    c2 = 300000000 * 300000000
    energy = int(c2 * int(to))
    print(energy)

main()