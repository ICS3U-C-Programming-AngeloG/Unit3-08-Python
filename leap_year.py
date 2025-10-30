#!/usr/bin/env python3

# Created by: Angelo Garcia
# Created on: October 30th, 2025
# Program checks if a given year is a leap year


def main():
    # This line asks the user to enter a year (keeps it as text)
    year_as_string = input("Enter a year: ")
    # Add a blank line for readability
    print("")

    try:
        # This line converts the input to a number
        year_as_number = int(year_as_string)

        # Check if the year is divisible by 4
        if year_as_number % 4 == 0:
            # Check if the year is divisible by 100
            if year_as_number % 100 == 0:
                # Check if the year is divisible by 400
                if year_as_number % 400 == 0:
                    # This line prints that it is a leap year
                    print("This is a leap year.")
                else:
                    # Prints that it is not a leap year
                    print("This is not a leap year.")
            else:
                # Prints that it is a leap year
                print("This is a leap year.")
        else:
            # Prints that it is not a leap year
            print("This is not a leap year.")

    except Exception:
        # This line runs if input is not a number
        print("That was not a number!")

    finally:
        # Prints a closing message
        print("Thank you for using the program.")


if __name__ == "__main__":
    main()
