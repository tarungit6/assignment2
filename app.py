def is_palindrome(word):
    # Remove whitespace and convert to lowercase
    word = word.replace(" ", "").lower()
    
    # Check if the word is equal to its reverse
    if word == word[::-1]:
        return True
    else:
        return False

# Test the function
input_word = input("Enter a word: ")
if is_palindrome(input_word):
    print(f"{input_word} is a palindrome!")
else:
    print(f"{input_word} is not a palindrome.")
