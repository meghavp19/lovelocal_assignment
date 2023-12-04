def find_elements_appearing_more_than_third(nums):
    result = []
    
    # Initialize candidate elements and their respective counts
    candidate1, candidate2, count1, count2 = 0, 1, 0, 0
    
    # Count occurrences of candidates in the array
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            # Set a new candidate if count1 is 0
            candidate1, count1 = num, 1
        elif count2 == 0:
            # Set a new candidate if count2 is 0
            candidate2, count2 = num, 1
        else:
            # Decrement counts if neither count1 nor count2 is 0
            count1 -= 1
            count2 -= 1
    
    # Reset counts for candidates and verify their occurrences
    count1, count2 = 0, 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
    
    # Check if candidates appear more than ⌊ n/3 ⌋ times and add them to the result
    if count1 > len(nums) // 3:
        result.append(candidate1)
    if count2 > len(nums) // 3:
        result.append(candidate2)
    
    return result

# Take input from the user
user_input = input("Enter integer array separated by spaces: ")

# Convert the input string to a list of integers
nums = list(map(int, user_input.split()))

# Call the function with user input
result = find_elements_appearing_more_than_third(nums)

# Display the result
print("Elements appearing more than ⌊ n/3 ⌋ times:", result)
