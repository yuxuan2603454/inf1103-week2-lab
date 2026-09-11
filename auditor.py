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
