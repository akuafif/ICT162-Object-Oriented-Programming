from PartTimeEmployee import PartTimeEmployee
from Manager import Manager, FullTimeEmployee

def printEmployees(employees) -> None:
    for v in employees.values():
        print(v)
        
def rotateWFH(employees: dict) -> None:
    for v in employees.values():
        v.workFromHome = False if v.workFromHome == 'Yes' else True

def main() -> None:
    # Creating Employee object and inserting into a dictionary
    employees = {}
    employees[101] = FullTimeEmployee(101, 'Jeff', False, 3)
    employees[102] = FullTimeEmployee(102, 'Jim', True, 3)
    employees[103] = PartTimeEmployee(103, 'Joe', False, 20)
    employees[104] = FullTimeEmployee(104, 'Jack', True, 2)
    employees[105] = FullTimeEmployee(105, 'Jane', False, 1)
    employees[106] = Manager(106, 'Tom', False, 4)
    employees[201] = Manager(201, 'Neil', False, 4)
    employees[205] = FullTimeEmployee(205, 'Charles', False, 4)
    employees[204] = PartTimeEmployee(204, 'Darren', True, 32)
    employees[203] = FullTimeEmployee(203, 'Elliot', False, 3)
    employees[202] = PartTimeEmployee(202, 'Fred', True, 10)
    
    print('Inital Data')
    printEmployees(employees)
    print('-' * 80) # line separator
    
    print('\nAfter WFH toggle')
    rotateWFH(employees)
    printEmployees(employees)
    print('-' * 80) # line separator
    
    
if __name__ == '__main__':
    main()