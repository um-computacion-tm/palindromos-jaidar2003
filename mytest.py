import unittest

from palindrome import palindrome
from palindromo import palindromo
class TestPalindrome(unittest.TestCase):

    def test_palindromo(self):
        result = palindromo('oso')
    def test_palindrome1(self):
        result = palindromo('neuquen') 
    def test_palindrome2(self):
        result = palindromo('radar')
    def test_palindrome4(self):
        result = palindromo('reconocer')
       
    def test_palindromoa(self):
        result = palindrome('oso')
    def test_palindromeb(self):
        result = palindrome('neuquen') 
    def test_palindromec(self):
        result = palindrome('radar')
    def test_palindromed(self):
        result = palindrome('reconocer') 

if __name__ == '__main__':
    unittest.main()
