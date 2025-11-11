# This program turns a list of numbers from 0-9 to the format of a phone number

# This is where the magic happens
def create_phone_number(n):  # The parts are divided into three
    nstr = list(map(str, n))
    string = "".join(nstr)
    # Checks if it is 10 digits and is only numeric
    if len(n) == 10 and string.isnumeric():
        # Gets each parts and turns it into a sting
        part1 = list(map(str, n[:3]))
        str1 = "".join(part1)

        part2 = list(map(str, n[3:6]))
        str2 = "".join(part2)

        part3 = list(map(str, n[6:]))
        str3 = "".join(part3)
            # Prints every thing in the corrent format
        print(f"({str1}) {str2}-{str3}")
    else:
        print("Please enter the correct format")

# Call the function
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
