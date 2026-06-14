def countdown(bottles):
    while bottles > 0:

        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            bottles -= 1
            print(f"Take one down and pass it around, {bottles} bottle(s) of beer on the wall.\n")

        elif bottles == 1:
            print(f"1 bottle of beer on the wall, 1 bottle of beer.")
            bottles -= 1
            print("Take one down and pass it around, 0 bottles of beer on the wall.\n")


def main():
    try:
        num = int(input("Enter number of bottles: "))
        countdown(num)

        print("Time to buy more bottles of beer.")

    except ValueError:
        print("Please enter a valid number.")


main()