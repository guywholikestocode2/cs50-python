def main():
    camel = input("camelCase: ")
    snake_case(camel)





def snake_case(camel):
    snake_string = ""
    for i in range(len(camel)):
        if camel[i].isupper():
         snake_string += f"_{camel[i].lower()}"
        else:
         snake_string += camel[i]

    print("snake_case:", snake_string)




main()
