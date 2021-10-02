from Company import Company
from FullTimeEmployee import FullTimeEmployee
from PartTimeEmployee import PartTimeEmployee
from Department import Department, Manager

def insertData(companySUSS : Company) -> None:
    deptIT = Department('IT Helpdesk', Manager(106, 'Tom', False, 4), True)
    deptMarketing = Department('Marketing', Manager(201, 'Neil', False, 4), False)
    
    deptIT.addEmployee(FullTimeEmployee(101, 'Jeff', False, 3))
    deptIT.addEmployee(FullTimeEmployee(102, 'Jim', True, 4))
    deptIT.addEmployee(PartTimeEmployee(103, 'Joe', False, 20))
    deptIT.addEmployee(FullTimeEmployee(104, 'Jack', True, 2))
    deptIT.addEmployee(FullTimeEmployee(105, 'Jane', False, 1))
    deptIT.addEmployee(FullTimeEmployee(105, 'Jane', False, 1))
    
    deptMarketing.addEmployee(FullTimeEmployee(205, 'Charles', False, 4))
    deptMarketing.addEmployee(PartTimeEmployee(204, 'Darren', True, 32))
    deptMarketing.addEmployee(FullTimeEmployee(203, 'Elliot', False, 3))
    deptMarketing.addEmployee(PartTimeEmployee(202, 'Fred', True, 10))
    
    companySUSS.addDepartment(deptIT)
    companySUSS.addDepartment(deptMarketing)

def main() -> None:
    companySUSS = Company('SUSS', 'EDU1002334')
    insertData(companySUSS)
     
    print('-' * 80) # line separator
    print('Inital Data')
    print('-' * 80) # line separator
    print(companySUSS)
    print('-' * 80) # line separator
    
    print('\n', '-' * 80, sep='') # line separator
    print('After Setting Safe Management Percentage to 40')
    print('-' * 80) # line separator
    companySUSS.setSafeManagePercentage(40)
    print(companySUSS)    
    print('-' * 80) # line separator
    
if __name__ == '__main__':
    main()