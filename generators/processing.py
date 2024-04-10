def process_transactions(filename, target_user_id):
    """Generator function to yield transaction amount for a specific user ID."""
    with open(filename, 'r') as file:
        for line in file:
            user_id, amount = line.strip().split(',')
            if int(user_id) == target_user_id:
                yield float(amount)

def calculate_total_for_user(filename, user_id):
    total = sum(process_transactions(filename, user_id))
    return total

filename = "large_log_file.txt"
target_user_id = 39
total_amount = calculate_total_for_user(filename, target_user_id)
print(f"Total amount for user {target_user_id}: {total_amount}")