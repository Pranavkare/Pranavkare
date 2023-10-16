def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s = s.replace(" ", "").lower()
    
    # Initialize two pointers, one at the beginning and one at the end of the string
    i, j = 0, len(s) - 1

    # Compare characters from the beginning and end, moving inward
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True

# Test the function
input_string = "A man a plan a canal Panama"
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")
This code defines a function is_palindrome that removes spaces and converts the string to lowercase to make the comparison case-insensitive. It then uses two pointers to compare characters from the beginning and end of the string until they meet in the middle. If all characters match, the string is a palindrome.






