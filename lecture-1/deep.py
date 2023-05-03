def main():
     life()


def life():
    q = input("What is the answer to the Great Question of Life, the Universe and Everything? ").lower().strip()
    match q:
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")
main()