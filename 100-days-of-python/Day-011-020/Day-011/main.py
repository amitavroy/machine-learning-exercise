def helloWorld(name):
    print("Hello there {}".format(name))

def is_palindrome(string: str) -> bool:
    """
    Checks if the provided string is a palindrome or not.
    :param string: The string that will be checked whether it is Palindrome or not.
    :return: Returns a boolean value whether the string is palindrome or not.
    """
    new_string = string.casefold()
    return new_string[::-1] == new_string


helloWorld("Amitav")
print()
print(is_palindrome('Dad'))
