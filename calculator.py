try:
    a=int(input("Enter the first number: "))
    b=int(input("Enter the first number: "))

    print(" What kind of operation do you need to perform. Press + for addition \nPress - for subtraction\nPress/for division\npress * for multiplication")

    o= input("Enter Operation:")
    match o:
        case"+":
            print(f" The result is: {a+b}")
        case"-":
            print(f" The result is: {a-b}")
        case"*":
            print(f" The result is: {a*b}")
        case"/":
            print(f" The result is: {a/b}")
        case default:
            print(f"There was an error")
            
except Exception as e:
    print(" Enter a valid value of a and b")
