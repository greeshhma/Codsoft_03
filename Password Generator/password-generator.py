from random import choice, shuffle
from string import ascii_letters, digits, punctuation
def pass_gen(length=8):
    """
    >>> len(pass_gen())8
    >>> len(pass_gen(length=16))16
    >>> len(pass_gen(257))257
    >>> len(pass_gen(length=0))0
    >>> len(pass_gen(-1))0
    """
    chars = tuple(ascii_letters) + tuple(digits) + tuple(punctuation)
    return "".join(choice(chars) for x in range(length))
def alternative_pass_gen(ctbi, i):
    i = i - len(ctbi)
    quotient = int(i / 3)
    remainder = i % 3
    chars = (
        ctbi
        + random(ascii_letters, quotient + remainder)
        + random(digits, quotient)
        + random(punctuation, quotient)
    )
    chars = list(chars)
    shuffle(chars)
    return "".join(chars)
def random(ctbi, i):
    return "".join(choice(ctbi) for x in range(i))
def random_number(ctbi, i):
    pass 
def random_letters(ctbi, i):
    pass 
def random_characters(ctbi, i):
    pass 
def main():
    length = int(input("Enter the length of password: ").strip())
    print("Password is generated of the desired length: ", pass_gen(length))   
if __name__ == "__main__":
    main()