import math as m

def main():
        
    a = int(input("Enter a no. "))
    print("")
    print(" + for add")
    print(" - for sub")
    print(" * for multiply")
    print(" / for division\n")
    print("lg for logarithm")
    
    choice = input("\nEnter the opertion: ")
    print("")
    b = int(input("Enter a no. "))
        
    if choice in ("+", "-", "*", "/","lg"):
            
        if choice == "+":
            print(a, '+', b,'=', a + b)

        if choice == "-":
            print(a - b)
            
        if choice == "*":
            print(a * b)
                
        if choice == "/":
            print(a / b)
        
        if choice == "lg":
            b = m.log(a) + m.log(b)
            print(b**10)

    else:
            print("Invalid choice")
            
main()
