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

    # Process a valid non-negative integer
    else:
        quantity = int(entry)
        inventory += quantity

        print(f"Quantity accepted. Current inventory: {inventory}")

        # Stop immediately if inventory exceeds 500
        if inventory > 500:
            print("OVERSTOCK ALERT: Inventory has exceeded 500 units!")
            break

# Display the final report
print("\nInventory Audit Report")
print(f"Total Units Processed: {inventory}")
print(f"Number of Failed/Rejected Entries: {failed_entries}")