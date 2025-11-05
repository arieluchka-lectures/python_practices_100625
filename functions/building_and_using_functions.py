# ============================================================
# PYTHON FUNCTIONS PRACTICE - Part 1: Building Functions
# ============================================================
# In this first part, you will create 5 functions that manipulate
# strings and lists. These functions will be used in Part 2.
# ============================================================


# FUNCTION 1: make_uppercase
# Create a function called make_uppercase that takes a string as input
# and returns the string in all uppercase letters.
# Example: make_uppercase("hello") should return "HELLO"





# FUNCTION 2: count_vowels
# Create a function called count_vowels that takes a string as input
# and returns the number of vowels (a, e, i, o, u) in the string.
# Count both lowercase and uppercase vowels.
# Example: count_vowels("Hello World") should return 3





# FUNCTION 3: reverse_string
# Create a function called reverse_string that takes a string as input
# and returns the string reversed.
# Example: reverse_string("python") should return "nohtyp"





# FUNCTION 4: remove_duplicates
# Create a function called remove_duplicates that takes a list as input
# and returns a new list with only unique elements (no duplicates).
# Keep the first occurrence of each element.
# Example: remove_duplicates([1, 2, 2, 3, 1, 4]) should return [1, 2, 3, 4]





# FUNCTION 5: get_longest_word
# Create a function called get_longest_word that takes a list of strings
# as input and returns the longest string from the list.
# If there are multiple strings with the same longest length, return the first one.
# Example: get_longest_word(["cat", "elephant", "dog"]) should return "elephant"







# ============================================================
# PYTHON FUNCTIONS PRACTICE - Part 2: Using Your Functions
# ============================================================
# Now use the functions you created above to solve these exercises.
# You will need to combine multiple functions together!
# ============================================================

# TEST DATA - Use these variables for the exercises below
sentence1 = "learning python is fun and exciting"
sentence2 = "I love to code in Python every day"
word_list = ["programming", "code", "debugging", "algorithm", "loop"]
mixed_list = ["apple", "banana", "apple", "orange", "banana", "grape", "apple"]
names = ["Alice", "bob", "CHARLIE", "david", "EVE"]


# EXERCISE 1:
# Take sentence1, convert it to uppercase using make_uppercase,
# then count how many vowels are in the uppercase version using count_vowels.
# Print the result.
# Expected output should be a number.




# EXERCISE 2:
# Take sentence2 and reverse it using reverse_string.
# Then convert the reversed sentence to uppercase using make_uppercase.
# Print the final result.




# EXERCISE 3:
# Take word_list and find the longest word using get_longest_word.
# Then reverse that longest word using reverse_string.
# Print the reversed longest word.




# EXERCISE 4:
# Take mixed_list and remove all duplicates using remove_duplicates.
# Then find the longest word from the unique list using get_longest_word.
# Finally, count the vowels in that longest word using count_vowels.
# Print the number of vowels.




# EXERCISE 5:
# Take the names list and do the following:
# 1. Convert each name to uppercase using make_uppercase (use a loop)
# 2. Store all uppercase names in a new list called uppercase_names
# 3. Find the longest name from uppercase_names using get_longest_word
# 4. Reverse that longest name using reverse_string
# 5. Print the final reversed name




# EXERCISE 6:
# Take sentence1, split it into a list of words (hint: use .split() method)
# Remove any duplicate words using remove_duplicates
# Find the longest unique word using get_longest_word
# Reverse it using reverse_string
# Convert it to uppercase using make_uppercase
# Print the final result




# EXERCISE 7:
# Create a new list called vowel_counts that contains the number of vowels
# in each word from word_list.
# Use count_vowels inside a loop to count vowels for each word.
# Then print the vowel_counts list.
# Also print which word has the most vowels (use the index of the max value)




# BONUS CHALLENGE:
# Take sentence2, reverse the entire sentence using reverse_string.
# Split the reversed sentence into words.
# Remove duplicates from the word list using remove_duplicates.
# For each unique word, count its vowels using count_vowels.
# Find the word with the maximum vowel count and print both the word and the count.



