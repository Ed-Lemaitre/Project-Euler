# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

from eulermodule import is_palindrome

pal = 1

for i in range(999):
    for j in range(999):
        num = (i+1)*(j+1)
        if num>pal and is_palindrome(str(num)):
            pal = num
print(pal)