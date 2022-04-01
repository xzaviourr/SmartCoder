
def check_prime(number):
    """
    Check if a number is prime
    """
    for i in range(2, number):
        if number%i == 0:
            return False
    return True
