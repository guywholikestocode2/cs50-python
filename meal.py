def main():
    x = input("What is the time? ").strip()
    h = convert(x)
    if h >= 7 and h <= 8:
        print("breakfast time")
    elif h >= 12 and h <= 13:
        print("lunch time")
    elif h >= 18 and h <= 19:
        print("dinner time")



def convert(time):
    h1, m = time.split(":")
    h1 = int(h1)
    m = int(m)
    m = float(m/60)
    return (h1 + m)



if __name__ == "__main__":
    main()