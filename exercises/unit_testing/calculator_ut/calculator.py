class Calculator():
    """
    Performs the four basic mathematical operations

    Methods:
     add(number, number)
     subtract(number, number)
     multiply(number, number)
     divide(number,number)
    """

    def add(self, firstOperand, secondOperand):
        """
        Adds two numbers together

        Arguments:
          firstOperand - Any number
          secondOperand - Any number
        """

        return firstOperand + secondOperand

    def subtract(self, num1, num2):
        """
        Subtract one number from another

        Arguments:
            num1 - Any number
            num2 - Any number
        """
        return num1 - num2

    def multiply(self, num1, num2):
        """
        Multiply two numbers together

        Arguments:
            num1 - Any number
            num2 - Any number
        """
        return num1 * num2

    def divide(self, num1, num2):
        """
        Divide two numbers

        Arguments:
            num1 - Any number
            num2 - Any number
        """
        return num1 / num2