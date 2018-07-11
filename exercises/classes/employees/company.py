class Company(object):
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded

    def get_company_name(self):
        """Returns the name of the company"""

        return self.company_name

    # Add the remaining methods to fill the requirements above