""" This file contains the main method for Question 3. """

from VaccinationLeave import VaccinationLeave
from Leave import Leave, LeaveApplicationException
from Company import Company
from FullTimeEmployee import FullTimeEmployee ,Employee
from PartTimeEmployee import PartTimeEmployee
from Department import Department, Manager
from typing import Union
from datetime import datetime

def insertData(company : Company) -> None:
    """ Initialise all the data based on Q3d(i).

    Args:
        companySUSS (Company): The Company object to be initialised with the data.
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
    
    company.addLeave(Leave(deptIT.searchEmployee(101),datetime(2021,6,30),datetime(2021,7,5)))
    company.addLeave(Leave(deptIT.searchEmployee(101),datetime(2021,7,15),datetime(2021,7,19)))
    company.addLeave(Leave(deptIT.searchEmployee(103),datetime(2021,6,29),datetime(2021,7,6)))
    company.addLeave(VaccinationLeave(deptIT.searchEmployee(104),datetime(2021,6,30),datetime(2021,6,30)))
    company.addLeave(Leave(deptIT.searchEmployee(105),datetime(2021,6,30),datetime(2021,7,5)))
    company.addLeave(Leave(deptIT.searchEmployee(105),datetime(2021,7,7),datetime(2021,7,22)))
    company.addLeave(VaccinationLeave(deptIT.searchEmployee(106),datetime(2021,6,30),datetime(2021,6,30)))
    company.addLeave(VaccinationLeave(deptIT.searchEmployee(106),datetime(2021,7,30),datetime(2021,7,30)))

    company.addLeave(Leave(deptMarketing.searchEmployee(201),datetime(2021,6,30),datetime(2021,7,5)))
    company.addLeave(VaccinationLeave(deptMarketing.searchEmployee(201),datetime(2021,7,6),datetime(2021,7,6)))
    company.addLeave(Leave(deptMarketing.searchEmployee(205),datetime(2021,6,30),datetime(2021,7,5)))
    company.addLeave(VaccinationLeave(deptMarketing.searchEmployee(201),datetime(2021,7,30),datetime(2021,7,30)))
    company.addLeave(Leave(deptMarketing.searchEmployee(204),datetime(2021,6,30),datetime(2021,7,5)))
    company.addLeave(Leave(deptMarketing.searchEmployee(204),datetime(2021,7,7),datetime(2021,7,15)))
    company.addLeave(Leave(deptMarketing.searchEmployee(203),datetime(2021,6,30),datetime(2021,7,5)))
    company.addLeave(Leave(deptMarketing.searchEmployee(203),datetime(2021,7,9),datetime(2021,7,13)))
    company.addLeave(Leave(deptMarketing.searchEmployee(202),datetime(2021,7,5),datetime(2021,7,8)))
    company.addLeave(Leave(deptMarketing.searchEmployee(202),datetime(2021,7,13),datetime(2021,7,13)))

def menu() -> int:
    """ Prints the main menu and returns the selection number.

    Returns:
        int: The option that the user choose.
    """
    while True:
        try:
            print('Menu\n'
                  '======\n'
                  '1. Apply Leave\n'
                  '2. Cancel Leave\n'
                  '3. Display Employee Leave Profile\n'
                  '4. Daily Movement Update\n'
                  '5. Update Safe Management Measure Percentage\n'
                  "6. Display Departments' SMM status\n"
                  '0. Exit')
            choice = convertInputToInt('Enter option: ')
            print()
            if choice != None and 0 <= choice <= 6:
                return choice
            else:
                print('Please enter a valid selection number\n')
        except:    
            print('Please enter a valid selection number\n')

def inputDate(message: str) -> datetime:
    """ Validate user input to be in datetime format and returns it.

    Args:
        message (str): The message to display upon calling input().

    Returns:
        datetime: The datetime object of the user inputted date.
    """
    while True:
        try:
            userInput = input(message)
            day, month, year = userInput.split('/')
            return datetime(year=int(year),month=int(month),day=int(day))
        except ValueError:
            print(f'{userInput} is not in the format dd/mm/yyyy')

def convertInputToInt(message: str) -> int:
    """ Converts user inputs into int type. If input is not digits, returns None.

    Args:
        message (str): The message to display upon calling input().

    Returns:
        int: The value of user input in int type if valid, otherwise None.
    """
    try:
        userInput = input(message)
        return int(userInput)
    except ValueError:
        return None

def getEmployeeAndDept(company: Company, employeeId: int, dept: str) -> Union[Employee, Department]:
    """ Retrieves the Employment and Department object from a Company Object.

    Args:
        company (Company): The Company Object to retrieve from.
        employeeId (int): The employee's ID to be search with.
        dept (str): The department name to be search with.

    Returns:
        Union[Employee, Department]: The employee and department object retrieved by the search.
    """
    employeeDept = company.searchDepartment(dept)
    if employeeDept == None:
        print('No matching department, please re-try')
        return None, None
    else:
        applicant = employeeDept.searchEmployee(employeeId)
        if applicant == None:
            print('No such employee, please re-try')
            return None, None
    return applicant, employeeDept

def applyLeave(company: Company, applicantId: int, dept: str) -> None:
    """ Adds a Leave object to the a Company object record.

    Args:
        company (Company): The Company object to be added into.
        applicantId (int): The applicant's ID of the leave request.
        dept (str): The department name that the applicant belongs to.

    Raises:
        LeaveApplicationException: Not allow to apply more than 2 vaccination leaves within same year.
    """
    if applicantId != None:    
        applicant, employeeDept = getEmployeeAndDept(company,applicantId,dept)
        if applicant != None and employeeDept != None:
            # Get dates and check for vaccination leave
            fromDate = inputDate('Enter from-date in dd/mm/yyyy: ')
            toDate = inputDate('Enter to-date in dd/mm/yyyy: ')     
            while True:
                vacLeave = input('Vaccination leave? (Y/N): ').upper()
                if vacLeave == 'Y' or vacLeave == 'N': 
                    break
                else: 
                    print('Invalid input, please re-try')
                    
            try:
                if vacLeave == 'Y':
                    if company.getVaccinationLeaveCount(applicantId, fromDate.year) >= 2:
                        raise LeaveApplicationException('Not allow to apply more than 2 vaccination leaves within same year') 
                    newLeave = VaccinationLeave(applicant,fromDate,toDate)
                else:
                    newLeave = Leave(applicant,fromDate,toDate)
                company.addLeave(newLeave)
                print(f'Leave Request Added!!\n{newLeave}')
            except LeaveApplicationException as e:
                print(e)
    else:
        print('Invalid employee ID input, please re-try')
            
def cancelLeave(company: Company, employeeId: int, leaveId: int) -> None:
    """ Cancels an approved leave request based on employeeId and leaveRequestId.

    Args:
        company (Company): The Company object that the employee belongs to.
        employeeId (int): The applicant's ID of the leave request.
        leaveId (int): The leave ID of the leave request.
    """
    if employeeId != None:
        try:
            company.cancelLeave(employeeId,leaveId)
            print(f'Leave request {leaveId} cancelled successfully')
        except LeaveApplicationException as e:
            print(e)
    else:
        print('Invalid employee ID input, please re-try')

def displayEmployeeLeaveProfile(company: Company, employeeId: int, dept: str) -> None:
    """ isplays all the employee's leave profile in the Company object

    Args:
        company (Company): The Company object to retrieve from.
        employeeId (int): The employee's ID to search with.
        dept (str): The department name that the applicant belongs to.
    """
    if employeeId != None:
        applicant, employeeDept = getEmployeeAndDept(company,employeeId,dept)
        if applicant != None and employeeDept != None:
            leaveList = company.getLeave(employeeId)
            print(f'\n{applicant}', end='')
            if len(leaveList) == 0:
                print('Employee has no leave request record')
            else:
                for l in leaveList:
                    print(f'\n{l}')
    else:
        print('Invalid employee ID input, please re-try')

def dailyMovementUpdate(company: Company, employeeId: int, dept:str) -> None:
    """ Shows the WFH status of an employee. Prompts if user want to change the status

    Args:
        company (Company): The Company object to retrieve from.
        employeeId (int): The employee's ID to search with.
        dept (str): The department name that the applicant belongs to.
    """
    if employeeId != None:
        applicant, employeeDept = getEmployeeAndDept(company,employeeId,dept)
        if applicant != None and employeeDept != None:
            print(f'Currect work from home status is {applicant.workFromHome}')

            while True:
                change = input('Change the status? (Y/N): ').upper()
                if change == 'Y':
                    applicant.workFromHome = not applicant.workFromHome
                    break
                elif change == 'N': 
                    break
                else: 
                    print('Invalid input, please re-try')
    else:
        print('Invalid employee ID input, please re-try')
        
def updateSMMPercentage() -> None:
    """ Updates the Safe Management Measure (0% - 100%) """
    
    print(f'Current Safe Mangement Measure % is {Company.getSafeManagePercentage():.1f}')
    
    while True:
        try:
            newPercentage = float(input('Enter new Safe Management Measure %: '))
            if 0 <= newPercentage <= 100: 
                break
            else: 
                raise ValueError
        except ValueError:
            print('Sorry, please re-enter within range (0, 100)')

    Company.setSafeManagePercentage(newPercentage)
    print(f'Safe Mangement Measure % updated to {newPercentage:.1f}')

def main() -> None:
    """ This method will creates a Company object, populates it with Department, Employee and Leave objects using the data provided by Q3d(i), before presenting a menu to the users. """
    
    companySUSS = Company('SUSS', 'EDU1002334')
    insertData(companySUSS)
    
    while True:
        choice = menu()
        if   choice == 0: break
        elif choice == 1: applyLeave(companySUSS, convertInputToInt('Enter Employee ID: '), input("Enter employee's department: "))
        elif choice == 2: cancelLeave(companySUSS, convertInputToInt('Enter employee ID: '), convertInputToInt('Enter leave request ID to cancel: '))
        elif choice == 3: displayEmployeeLeaveProfile(companySUSS, convertInputToInt('Enter employee ID: '), input("Enter employee's department: "))
        elif choice == 4: dailyMovementUpdate(companySUSS, convertInputToInt('Enter employee ID: '), input("Enter employee's department: "))
        elif choice == 5: updateSMMPercentage()
        elif choice == 6: print(companySUSS)
        print()

if __name__ == '__main__':
    main()