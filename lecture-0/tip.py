def main():
    dollars = dollars_to_float(input("How much was the meal? ")) # Asking the user the cost of the meal
    percent = percent_to_float(input("What percentage would you like to tip? ")) # Asking the user the percentage of the cost they would like to tip
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

#Function for converting dollars from str to float
def dollars_to_float(d):
    d = d.replace("$", "")
    d = float(d)
    return d

#Function for converting the percentage from str to float
def percent_to_float(p):
    p = p.replace("%", "")
    p = float(p)
    p = p / 100
    return p


main()
