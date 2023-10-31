import math

def is_prime(n):
    """
    Check if a number is prime.

    This function takes an integer as input and returns True if the number
    is prime, and False if it's not.

    Args:
        n (int): The integer to be checked for primality.

    Returns:
        bool: True if the number is prime, False otherwise.

    Example:
        To check if the number 17 is prime, you can use this function as follows:

        >>> is_prime(17)
        True

        To check if the number 15 is prime:

        >>> is_prime(15)
        False
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
