#  PRACTICE: Pizza Joint
class Pizza:

    def __init__(self):

        self.toppings = []
        self.crust_type = ""
        self.size = ""

    def add_topping(self, *args):
        self.toppings += args 
        
    def pizza_description(self):
        top = " , ".join(self.toppings)
        print(f'You ordered a {self.size}, {self.crust_type} pizza with {top} as your topping(s).')


custom_pizza = Pizza()
custom_pizza.add_topping("cheese")
custom_pizza.add_topping("sausage")
custom_pizza.add_topping("pepperoni")
custom_pizza.add_topping("mushrooms")
custom_pizza.crust_type = "thin crust"
custom_pizza.size = "large"

# custom_pizza.pizza_description()

deep_dish_pizza = Pizza()
deep_dish_pizza.add_topping("cheese")
deep_dish_pizza.add_topping("sausage")
deep_dish_pizza.crust_type = "deep dish"
deep_dish_pizza.size = "medium"

# deep_dish_pizza.pizza_description()


# PRACTICE: Urban Planner
import datetime

class Building:

    def __init__(self, address, stories):
        self.designer = ""
        self.date_constructed = 0
        self.owner = ""
        self.address = address
        self.stories = stories

    def construct(self):
        self.date_constructed = datetime.datetime.now()

    def purchase(self, buyer):
        self.owner = buyer

    def building_info(self):
        print(f'{self.address} was purchased by {self.owner} on {self.date_constructed.strftime("%x")} and has {self.stories} stories')

interstate_blvd = Building("500 Interstate Blvd", 4)
interstate_blvd.purchase("John Wark")
interstate_blvd.construct()
interstate_blvd.building_info()

wallaby_way = Building("P. Sherman 42 Wallaby Way", 20)
wallaby_way.purchase("Dory")
wallaby_way.construct()
wallaby_way.building_info()

privet_drive = Building("4 Privet Drive", 2)
privet_drive.purchase("Vernon and Petunia Dursley")
privet_drive.construct()
privet_drive.building_info()
 

# PRACTICE: Companies and Employees
class Employee:

    def __init__(self, name, title, date):
        self.name = name
        self.job_title = title
        self.start_date = date

class Company:
    def __init__(self, name, address, type):
        self.name = name
        self.address = address
        self.type = type
        self.employee = list()

apple = Company("Apple", "100 Who Cares Dr", "Technology")
microsoft = Company("Microsoft", "Nobody GAF Blvd", "Technology")

em1 = Employee("Bryan", "Software Developer", datetime.datetime.now())
em2 = Employee("Sam", "Graphic Designer", datetime.datetime.now())
em3 = Employee("Linda","Software Developer", datetime.datetime.now())
em4 = Employee("Bob", "Security Analyst", datetime.datetime.now())
em5 = Employee("Susan", "Tech Support", datetime.datetime.now())

apple.employee.append(em1)
apple.employee.append(em2)

microsoft.employee.append(em3)
microsoft.employee.append(em4)
microsoft.employee.append(em5)


companies = []
companies.append(apple)
companies.append(microsoft)

for company in companies:
    print(f'{company.name} is in the {company.type} industry and has the following employees:')

    for emp in company.employee:
        print(f' * {emp.name}')




