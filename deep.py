def main():
    # Prompt for input
    user_input = input("Enter a number or a word: ").strip().lower()  # Strip spaces and convert to lowercase

    # Replace any hyphens with spaces to handle inputs like 'forty-two'
    user_input = user_input.replace("-", " ")

    # Check if the input is '42' or 'forty two'
    if user_input == "42" or user_input == "forty two":
        print("Yes")
    else:
        print("No")

main()


