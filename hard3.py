def count_ones_in_range(limit):
    ones_count = 0

    # Iterate through each number from 1 to the given limit (inclusive)
    for num in range(1, limit + 1):
        current_digit = num
        # Iterate through each digit in the current number
        while current_digit > 0:
            # Check if the rightmost digit is 1
            if current_digit % 10 == 1:
                ones_count += 1
            # Move to the next digit place value
            current_digit //= 10

    return ones_count

# Take input from the user
user_limit = int(input("Enter a non-negative integer: "))

# Call the function with user input
result_count = count_ones_in_range(user_limit)

# Display the result
print("Total occurrences of digit 1:", result_count)
