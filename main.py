from calculator import add, subtract, multiply, divide

def show_menu():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")


def run():
    show_menu()

    try:
        choice = int(input("Enter your choice (1-4): "))
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))

        if choice == 1:
            result = add(number1, number2)
        elif choice == 2:
            result = subtract(number1, number2)
        elif choice == 3:
            result = multiply(number1, number2)
        elif choice == 4:
            result = divide(number1, number2)
        else:
            print("Invalid option")
            return

        print("Result:", result)

    except ValueError as error:
        print("Error:", error)
    except Exception:
        print("Something went wrong")


if __name__ == "__main__":
    run()
