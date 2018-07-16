class Company():
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded

        self.employees = set() #declaring an empty set

    def get_company_name(self):
        """Returns the name of the company"""

        return self.company_name

    def get_date_founded(self):
        """Returns the date founded of the company"""

        return self.date_founded

    def employee_list(self):
        employee_group = ""

        for e in self.employees:
            employee_group += {e.employee_name}

        return employee_group

    # def __str__(self): #str method always needs to be part of the class -- how to format
    #     employee_list = ""
    #     for e in self.employees:
    #         employee_list += {e.employee_name}
    #     return (f"{self.company_name}, {employee_list}")
