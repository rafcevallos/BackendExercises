import unittest
from palindrome import Palindrome


class PalindromeTest(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_fun_returns_8(self):
        self.assertEqual(palindrome.fun(8), 8)

    def test_is_palindrome(self):
        pal = Palindrome() #creates an instance of Palindrome
        self.assertTrue(pal.is_palindrome("mom"))
        # self.assertTrue(pal.is_palindrome("MOM"))
        # self.assertTrue(pal.is_palindrome("A but tuba"))
        # self.assertTrue(pal.is_palindrome(2))

if __name__ == '__main__':
    unittest.main()