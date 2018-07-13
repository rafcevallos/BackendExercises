# Notes: Classes are blueprints for building objects.  You can combine information and heaviors
# a single namespace.  You can create multiple instances of that CLASS in the form of objects,
# which will have the same info/behavior

# 1. Create a class that contains information about employees of a company and define methods to get/set employee name, job title, and start date.


class Employee():
    """
    Contains methods for maintaining Employees

    Methods:
    --------
    get_employee_name
    get_job_title
    get_start_date

    set_employee_name
    set_job_title
    set_start_date

    """

# __init__ looks like a constructor function BUT IT'S NOT
# It only gets invoked after the instance of the class has been fully created, and that new instance gets passed into the __init__ function.
    def __init__(self, employee_name, job_title, start_date):
        self.employee_name: employee_name
        self.job_title: job_title
        self.start_date: start_date

    def get_employee_name(self):
        """Returns the name of the employee"""
        return self.employee_name

    def get_job_title(self):
        """Returns the job title"""
        return self.job_title

    def get_start_date(self):
        """Returns the employee start date"""
        return self.start_date

    def set_employee_name(self, employee_name):
        """
        Sets the name of the employee

        Method argument:
        ----------------
        employee_name(string) -- The employee name to add
        """
        self.employee_name = employee_name

    def set_job_title(self, job_title):
        """
        Sets the job title of the employee

        Method argument:
        ----------------
        job_title(string) -- The job title of the employee
        """
        self.job_title = job_title

    def set_start_date(self, start_date):
        """
        Sets the start date of the employee

        Method argument:
        ----------------
        start_date(string) -- The job start date of the employee
        """
        self.start_date = start_date