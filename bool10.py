import math
def main(a):
    """check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here

    # haqiqiy kvadrat ildiz raqami ekanini tekshiradi
    # qoldiq qolmasa ildiz haqiqiy hisoblanadi
    return (math.sqrt(a) % 1) == 0

print(main(16))