class y(Exception):
    """Base class for other exceptions"""
class ValueTooSmallError(y):
    """Raised when the input value is too small"""
class ValueTooLargeError(y):
    """Raised when the input value is too large"""
number = 10
# user guesses a number until he/she gets it right
while True:
    try:
        x = int(input("Enter a number: "))
        if x < number:
            raise ValueTooSmallError
        elif x > number:
            raise ValueTooLargeError
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print()

print("Congratulations! You guessed it correctly.")
"""
creating a base class is compulsory
output:
Enter a number: 12
This value is too large, try again!

Enter a number: 0
This value is too small, try again!

Enter a number: 8
This value is too small, try again!

Enter a number: 10
Congratulations! You guessed it correctly.
"""
