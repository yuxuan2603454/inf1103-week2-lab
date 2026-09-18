def get_valid_input():
    while True:
        user_input = input("Enter stock quantity (or 'quit' to exit): ")

        if user_input.lower() == "quit":
            return "quit"

        if not user_input.isdigit():
            print("Error: Please enter a valid positive integer.")
            continue

        return int(user_input)