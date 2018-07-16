from employees import Employee
from company import Company


if __name__ == '__main__':
    # Create a Company
    ThePoopStore = Company("The Poop Store", "7/17/77")

    # Create some EMPLOYEES
    raf = Employee("Raf", "Pooper Scooper", "01/27/2018")
    meghan = Employee("Meghan", "Sharking", "02/01/2018")
    deanna = Employee("Deanne", "Guru'ing", "5/15/2017")
    erin = Employee("Erin", "Food", "08/29/2016")

    # Add EMPLOYEES into the AGGREGATE instance variable of the COMPANY
    ThePoopStore.employees.add(raf)
    ThePoopStore.employees.add(meghan)
    ThePoopStore.employees.add(deanna)
    ThePoopStore.employees.add(erin)


print(ThePoopStore)