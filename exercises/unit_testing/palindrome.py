
def fun(num):
    return num

class Palindrome():
    def is_palindrome(self, source_string):

        reverse_string = source_string[::-1]
        # print(reverse_string)
        return source_string == reverse_string