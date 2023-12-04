# lovelocal_assignment
1)Easy 1: easy1.py

Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal 
substring consisting of non-space characters only.
Constraints:
1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
_____________________________________________________________________
Explaination of code:
_____________________________________________________________________
* This line starts the definition of a function named length_of_last_word that takes a 
  string s as an argument.
* The input string s is stripped of both trailing and leading spaces using the strip() 
  method, and the result is stored in the variable cleaned_string.
* A variable named last_word_length is initialized to store the length of the last word. 
  This will be updated as we iterate through the string.
* A for loop is initiated to iterate through the characters of the cleaned string from right 
  to left. char_index represents the index of the current character in the iteration.
* Within the loop, it checks if the current character (at char_index) is not a space.
* If the current character is not a space, it enters a nested while loop. This loop 
  increments last_word_length while the characters of the last word are encountered (moving 
  from right to left).
*  The while loop is exited with a break statement once the last word is identified, i.e., 
   when a space is encountered after the last word.
*  Finally, the function returns the calculated length of the last word.
*  The user is prompted to enter a string, and the input is stored in the variable 
   user_input.
*  The function length_of_last_word is called with the user's input, and the result is 
   stored in the variable result.

===============================================================
2) Medium 2 : medium2.py
  Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. 
  Constraints:
        1 <= nums.length <= 5 * 104
        -109 <= nums[i] <= 109
____________________________________________________________________________________
Explaination of code:
____________________________________________________________________________________

* def find_elements_appearing_more_than_third(nums):

* Defines a function named find_elements_appearing_more_than_third that takes a list of 
  integers (nums) as input.
  result = []

* Initializes an empty list named result to store the elements that appear more than one- 
  third of the times.
  candidate1, candidate2, count1, count2 = 0, 1, 0, 0

* Initializes four variables (candidate1, candidate2, count1, count2) to keep track of two 
  potential candidates and their respective counts.
  for num in nums:

* Iterates through each element (num) in the input list nums.
  if num == candidate1:

* Checks if the current element is equal to candidate1.
  count1 += 1

* Increments the count of candidate1 if the current element matches.
  elif num == candidate2:

*  Checks if the current element is equal to candidate2.
   count2 += 1

*  Increments the count of candidate2 if the current element matches.
   elif count1 == 0:

*  Checks if the count of candidate1 is zero.
   candidate1, count1 = num, 1

*  Sets a new candidate (candidate1) and initializes its count to 1 if the count of 
   candidate1 is zero.
   elif count2 == 0:

*  Checks if the count of candidate2 is zero.
   candidate2, count2 = num, 1

* Sets a new candidate (candidate2) and initializes its count to 1 if the count of 
  candidate2 is zero.
  else:

* Executes if none of the above conditions are met.
  count1 -= 1

* Decrements the count of candidate1.
  count2 -= 1

* Decrements the count of candidate2.
  count1, count2 = 0, 0

* Resets the counts of both candidates.
  for num in nums:

* Iterates through each element (num) in the input list nums again.
  if num == candidate1:

* Checks if the current element is equal to the first candidate.
  count1 += 1

* Increments the count of the first candidate.
  elif num == candidate2:

*  Checks if the current element is equal to the second candidate.
   count2 += 1

*  Increments the count of the second candidate.
   if count1 > len(nums) // 3:

*  Checks if the count of the first candidate is greater than one-third of the length of 
   the input list.
   result.append(candidate1)

*  Adds the first candidate to the result list if it appears more than one-third of the 
   times.
   if count2 > len(nums) // 3:

*  Checks if the count of the second candidate is greater than one-third of the length of 
   the input list.
   result.append(candidate2)

*  Adds the second candidate to the result list if it appears more than one-third of the 
   times.
   return result

*  Returns the list of elements that appear more than one-third of the times.
   user_input = input("Enter integer array separated by spaces: ")

*  Takes input from the user, expecting a string of integers separated by spaces.
   nums = list(map(int, user_input.split()))

*  Converts the input string to a list of integers.
   result = find_elements_appearing_more_than_third(nums)

*  Calls the function with the user's input and stores the result.
   print("Elements appearing more than ⌊ n/3 ⌋ times:", result)

========================================================
3) Hard 3:hard3.py
   Given an integer n, count the total number of digit 1 appearing in all non-negative 
   integers less than or equal to n.
   Constraints:
         0 <= n <= 109
______________________________________________________________________________________
Explaination of code:
______________________________________________________________________________________
* def count_ones_in_range(limit):

* Defines a function named count_ones_in_range that takes a non-negative integer limit as 
  input.
  ones_count = 0

* Initializes a variable named ones_count to keep track of the total occurrences of the 
  digit 1.
  for num in range(1, limit + 1):

* Initiates a loop that iterates through each number from 1 to the given limit (inclusive).
  current_digit = num

* Assigns the current number in the iteration to a variable named current_digit.
  while current_digit > 0:

* Initiates a loop that iterates through each digit in the current number until there are 
  no more digits.
  if current_digit % 10 == 1:

* Checks if the rightmost digit of the current number is equal to 1.
  ones_count += 1

* Increments the ones_count if the rightmost digit is 1.
  current_digit //= 10

* Updates the current_digit to move to the next digit place value (right to left).
  return ones_count

* Returns the total count of occurrences of the digit 1 in all the numbers from 1 to the 
  given limit.
  user_limit = int(input("Enter a non-negative integer: "))

* Prompts the user to enter a non-negative integer and converts the input to an integer 
  (int).
  result_count = count_ones_in_range(user_limit)

* Calls the function count_ones_in_range with the user's input (user_limit) and stores the 
  result in the variable result_count.
  print("Total occurrences of digit 1:", result_count)

* Displays the total occurrences of the digit 1 in all numbers from 1 to the user-provided 
  limit.
===================================================== 







