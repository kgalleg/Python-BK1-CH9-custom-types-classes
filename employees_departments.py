import datetime

# Instructions:

# Practice: Companies and Employees

# Instructions
# Create an Employee type that contains information about employees of a company. Each employee must have a name, job title, and employment start date.
# Create a Company type that employees can work for. A company should have a business name, address, and industry type.
# Create two companies, and 5 people who want to work for them.
# Assign 2 people to be employees of the first company.
# Assign 3 people to be employees of the second company.
# Output a report to the terminal the displays a business name, and its employees.
# For example:

# Acme Explosives is in the chemical industry and has the following employees
#    * Michael Chang
#    * Martina Navritilova

# Jetways is in the transportation industry and has the following employees
#    * Serena Williams
#    * Roger Federer
#    * Pete Sampras


class Employee:
    def __init__(self, emp_name,title, start):
        self.emp_name = emp_name
        self.job_title = title
        self.start_date = start

class Company:
    def __init__(self, buss_name, industry):
        self.buss_name = buss_name
        self.address = ""
        self.industry_type = industry
        self.employees = list()


life_way = Company("LifeWay", "Publishing")
home_depot = Company("HomeDepot", "Building Materials")

mimi = Employee("Mimi Chu", "Sales Manager", datetime.datetime.now())
jay = Employee("Jay Galleg", "Engineer", datetime.datetime.now())

tedy = Employee("Teddy Anders", "Admin", datetime.datetime.now())
vince = Employee("Vince Smith", "Finance Analyst", datetime.datetime.now())
peter = Employee("Peter McDonald", "Farmer", datetime.datetime.now())

life_way.employees.append(mimi)
life_way.employees.append(jay)

home_depot.employees.append(tedy)
home_depot.employees.append(vince)
home_depot.employees.append(peter)

# companies = []
# companies.append(life_way)
# companies.append(home_depot)

print(f'{life_way.buss_name} is a {life_way.industry_type} industry and has the following employees:')
for employee in life_way.employees:
    print(f"* {employee.emp_name}")

print(f'{home_depot.buss_name} is a {home_depot.industry_type} industry and has the following employees:')
for employee in home_depot.employees:
    print(f"* {employee.emp_name}")






