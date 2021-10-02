""" This file contains the main method for Question 1 """

from PartTimeEmployee import PartTimeEmployee
from Manager import Manager, FullTimeEmployee

def printEmployees(employees: list) -> None:
    """ Prints the employee list\n
    Args:
        employees ([list]): the list that holds all the employee object"""
    for e in employees:
        print(e)
        
def rotateWFH(employees: list) -> None:
    """ Rotate all the employee work from home status\n
    Args:
        employees ([list]): the list that holds all the employee object"""
    for e in employees:
        e.workFromHome = not e.workFromHome

def main() -> None:
    """ This function will print all the employee object based on Q1d(i).\n
        It will also toggleWFH status for each employee and print all the objects again """

    # Intialising all the object based on Q1d(i)
    employees = []
    employees.append(FullTimeEmployee(101, 'Jeff', False, 3))
    employees.append(FullTimeEmployee(102, 'Jim', True, 3))
    employees.append(PartTimeEmployee(103, 'Joe', False, 20))
    employees.append(FullTimeEmployee(104, 'Jack', True, 2))
    employees.append(FullTimeEmployee(105, 'Jane', False, 1))
    employees.append(Manager(106, 'Tom', False, 4))
    employees.append(Manager(201, 'Neil', False, 4))
    employees.append(FullTimeEmployee(205, 'Charles', False, 4))
    employees.append(PartTimeEmployee(204, 'Darren', True, 32))
    employees.append(FullTimeEmployee(203, 'Elliot', False, 3))
    employees.append(PartTimeEmployee(202, 'Fred', True, 10))
    
    print('-' * 80,'Inital Data','-' * 80, sep='\n') 
    printEmployees(employees)
    print('-' * 80) 

    # Toggling all the employee status
    print('', '-' * 80,'After WFH toggle','-' * 80, sep='\n') 
    rotateWFH(employees)
    printEmployees(employees)
    print('-' * 80) 
    
if __name__ == '__main__':
    main()