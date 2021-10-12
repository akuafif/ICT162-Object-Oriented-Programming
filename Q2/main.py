""" This file contains the main method for Question 2. """

from Company import Company
from FullTimeEmployee import FullTimeEmployee
from PartTimeEmployee import PartTimeEmployee
from Department import Department, Manager

def insertData(company : Company) -> None:
    """ Intialising the Department and Employee objects based on Q2c(i) requirements.

    Args:
        company (Company): The Company object to be associated with the intialised data.
    """
    deptIT = Department('IT Helpdesk', Manager(106, 'Tom', False, 4), True)
    deptMarketing = Department('Marketing', Manager(201, 'Neil', False, 4), False)
    
    deptIT.addEmployee(FullTimeEmployee(101, 'Jeff', False, 3))
    deptIT.addEmployee(FullTimeEmployee(102, 'Jim', True, 4))
    deptIT.addEmployee(PartTimeEmployee(103, 'Joe', False, 20))
    deptIT.addEmployee(FullTimeEmployee(104, 'Jack', True, 2))
    deptIT.addEmployee(FullTimeEmployee(105, 'Jane', False, 1))
    
    deptMarketing.addEmployee(FullTimeEmployee(205, 'Charles', False, 4))
    deptMarketing.addEmployee(PartTimeEmployee(204, 'Darren', True, 32))
    deptMarketing.addEmployee(FullTimeEmployee(203, 'Elliot', False, 3))
    deptMarketing.addEmployee(PartTimeEmployee(202, 'Fred', True, 10))
    
    company.addDepartment(deptIT)
    company.addDepartment(deptMarketing)

def main() -> None:
    """ This function will print all the Department and Employee object based on Q2c(i).\n
        It will also set a new Safe Management to 40% for each Department object and print all the objects again. 
    """
    companySUSS = Company('SUSS', 'EDU1002334')
    insertData(companySUSS)
     
    print('-' * 80,'Inital Data','-' * 80, sep='\n') 
    print(companySUSS)
    print('-' * 80) 
    
    print('', '-' * 80,'After Setting Safe Management Percentage to 40','-' * 80, sep='\n') 
    companySUSS.setSafeManagePercentage(40)
    print(companySUSS)    
    print('-' * 80)
    
if __name__ == '__main__':
    main()