# We will reverse the string and check if original str is same as reversed str

# We will iterate through the string and check if each char is an alphanumeric. In this solution we
# use python's built-in function

def is_palindrome(s):
    new_str = ""

    for c in s:
        if c.isalnum():
            new_str += c.lower()

    return new_str == new_str[::-1]


result = is_palindrome("amanaplanacanalpanama")
print(result)
