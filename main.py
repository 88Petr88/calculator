import tools


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return float(x) / float(y)


def main():
    while True:
        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5. Add from file")

        choice = input("Enter choice (1, 2, 3, 4, 5)")
        print(choice)

        if choice in ("1", "2", "3", "4", "5"):
            if choice == "5":
                nums = tools.load_nums_from_file()
                for pair in nums:
                    x = pair[0]
                    y = pair[1]
                    print(f"{x} + {y} = {add(x, y)}")
            else:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                if choice == "1":
                    print(f"{x} + {y} = {add(x, y)}")
                elif choice == "2":
                    print(f"{x} - {y} = {subtract(x, y)}")
                elif choice == "3":
                    print(f"{x} * {y} = {multiply(x, y)}")
                elif choice == "4":
                    print(f"{x} / {y} = {divide(x, y)}")
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()
