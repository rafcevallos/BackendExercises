class Company():
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded

        self.employees = set()

    def get_company_name(self):
        """Returns the name of the company"""

        return self.company_name

    def get_date_founded(self):
        """Returns the date founded of the company"""

        return self.date_founded
