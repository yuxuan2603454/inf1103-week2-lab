def get_valid_input():
    while True:
        user_input = input("Enter stock quantity (or 'quit' to exit): ")

        if user_input.lower() == "quit":
            return "quit"

        if not user_input.isdigit():
            print("Error: Please enter a valid positive integer.")
            continue

        return int(user_input)

def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total

def calculate_tax(amount):
    tax = amount * 0.10
    return tax

def generate_report(total_units, failed_attempts):
    print("\n--- Final Report ---")
    print("Total Deliveries Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)