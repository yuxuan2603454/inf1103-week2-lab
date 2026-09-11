# Start the inventory and rejected-entry counter at zero
inventory = 0
failed_entries = 0

# Continue asking for input until the loop is stopped
while True:
    entry = input(
        "Enter stock quantity (or type 'quit'): "
    ).strip()

    # Stop when the user types quit
    if entry.lower() == "quit":
        break

    # Reject negative integers
    elif entry.startswith("-") and entry[1:].isdigit():
        print("Error: Negative quantities are not allowed.")
        failed_entries += 1
        continue

    # Reject text and other invalid input
    elif not entry.isdigit():
        print("Error: Please enter a valid integer.")
        failed_entries += 1
        continue

