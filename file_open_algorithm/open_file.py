# Defines to the user the correct format the names should be written in
names = input("Please enter names in the format <david, john..>: ")

# Turns the names into a list
names_list = list(names.split(", "))  # cuts out the ',' and " " char


# Opens a new file and writes to it
with open("names_file.txt", "w") as file:
    for name in names_list: # Checks the integrity of each name
        if name.isalpha(): # Check if it only contain characters
            # Adds a new line to the file
            name += "\n"
            # Capitalize name
            capitalized_name = name.capitalize()
            # Writes to the file
            file.write(capitalized_name)
            print("Names written to file - Overrode old names\n")
        else: # If requirements not met, print("<Error Message>")
            print("Sorry type correct format")

# Prints contents of the file
with open("names_file.txt", "r") as file:
    print(file.read()) # Prints out the file
