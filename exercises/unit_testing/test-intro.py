# we make tests to design the code first aka what it should like (naming conventions, etc)
# instead of having your team wait for PERFECT, DYNAMIC code, you give them a function, for example, that prints out a hard-coded object.

# Red --> Green --> Refactor
import unittest

def fun(num):
    return num

class MyTest(unittest.TestCase):
    def test_fun_returns_8(self):
        self.assertEqual(fun(8), 8)

# This comparison will execute this file directly rather than importing as a module.  if you impmort a file, do not do this.
if __name__ == '__main__':
    unittest.main()
