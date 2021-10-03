import math as m

def main():
        
    a = int(input("Enter a no. "))
    print("")
    print(" + for add")
    print(" - for sub")
    print(" * for multiply")
    print(" / for division\n")
    
    choice = input("\nEnter the opertion: ")
    print("")
    b = int(input("Enter a no. "))
        
    if choice in ("+", "-", "*", "/",):
            
        if choice == "+":
            print(a, '+', b,'=', a + b)

        if choice == "-":
            print(a - b)
            
        if choice == "*":
            print(a * b)
                
        if choice == "/":
            print(a / b)
    else:
            print("Invalid choice")
            
main()
