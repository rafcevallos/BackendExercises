# Notes: Classes are blueprints for building objects.  You can combine information and heaviors
# a single namespace.  You can create multiple instances of that CLASS in the form of objects,
# which will have the same info/behavior

# 1. Create a class that contains information about employees of a company and define methods to get/set employee name, job title, and start date.


class Employee():
    """Contains methods for maintaining Employees

    Methods:
    --------
    get_employee_name
    get_job_title
    get_start_date
    """

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

    def set_employee_name(self):
        """Sets the name of the employee"""
        return self.employee_name

print(get_employee_name())
