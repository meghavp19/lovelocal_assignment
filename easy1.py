# Define a function to calculate the length of the last word in a given string
def length_of_last_word(s):
    # Remove trailing and leading spaces from the input string
    cleaned_string = s.strip()

    # Initialize a variable to store the length of the last word
    last_word_length = 0

    # Iterate through the characters in the cleaned string from right to left
    for char_index in range(len(cleaned_string) - 1, -1, -1):
        # Check if the current character is not a space
        if cleaned_string[char_index] != ' ':
            # Increment the length of the last word until a space is encountered
            while char_index >= 0 and cleaned_string[char_index] != ' ':
                last_word_length += 1
                char_index -= 1
            # Break the loop once the last word is identified
            break

    # Return the length of the last word
    return last_word_length

# Take input from the user
user_input = input("Enter a string: ")

# Call the function with user input
result = length_of_last_word(user_input)

# Display the result
print("Length of the last word:", result)
