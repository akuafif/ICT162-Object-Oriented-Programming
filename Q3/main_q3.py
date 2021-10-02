from typing import Union
from VaccinationLeave import VaccinationLeave, Leave, LeaveApplicationException
from datetime import datetime
from Company import Company
from FullTimeEmployee import FullTimeEmployee ,Employee
from PartTimeEmployee import PartTimeEmployee
from Department import Department, Manager

def insertData(companySUSS : Company) -> None:
    """ Initialise all the data based on question 3 instruction """

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
    
    companySUSS.addDepartment(deptIT)
    companySUSS.addDepartment(deptMarketing)
    
    companySUSS.addLeave(Leave(deptIT.searchEmployee(101),datetime(2021,6,30),datetime(2021,7,5)))
    companySUSS.addLeave(Leave(deptIT.searchEmployee(101),datetime(2021,7,15),datetime(2021,7,19)))
    companySUSS.addLeave(Leave(deptIT.searchEmployee(103),datetime(2021,6,29),datetime(2021,7,6)))
    companySUSS.addLeave(VaccinationLeave(deptIT.searchEmployee(104),datetime(2021,6,30),datetime(2021,6,30)))
    companySUSS.addLeave(Leave(deptIT.searchEmployee(105),datetime(2021,6,30),datetime(2021,7,5)))
    companySUSS.addLeave(Leave(deptIT.searchEmployee(105),datetime(2021,7,7),datetime(2021,7,22)))
    companySUSS.addLeave(VaccinationLeave(deptIT.searchEmployee(106),datetime(2021,6,30),datetime(2021,6,30)))
    companySUSS.addLeave(VaccinationLeave(deptIT.searchEmployee(106),datetime(2021,7,30),datetime(2021,7,30)))

    companySUSS.addLeave(Leave(deptMarketing.searchEmployee(201),datetime(2021,6,30),datetime(2021,7,5)))
    companySUSS.addLeave(VaccinationLeave(deptMarketing.searchEmployee(201),datetime(2021,7,6),datetime(2021,7,6)))
    companySUSS.addLeave(Leave(deptMarketing.searchEmployee(205),datetime(2021,6,30),datetime(2021,7,5)))
    companySUSS.addLeave(VaccinationLeave(deptMarketing.searchEmployee(201),datetime(2021,7,30),datetime(2021,7,30)))
    companySUSS.addLeave(Leave(deptMarketing.searchEmployee(204),datetime(2021,6,30),datetime(2021,7,5)))
    companySUSS.addLeave(Leave(deptMarketing.searchEmployee(204),datetime(2021,7,7),datetime(2021,7,15)))
    companySUSS.addLeave(Leave(deptMarketing.searchEmployee(203),datetime(2021,6,30),datetime(2021,7,5)))
    companySUSS.addLeave(Leave(deptMarketing.searchEmployee(203),datetime(2021,7,9),datetime(2021,7,13)))
    companySUSS.addLeave(Leave(deptMarketing.searchEmployee(202),datetime(2021,7,5),datetime(2021,7,8)))
    companySUSS.addLeave(Leave(deptMarketing.searchEmployee(202),datetime(2021,7,13),datetime(2021,7,13)))

def menu() -> int:
    """ Prints the main menu and returns the selection number """
    while True:
        try:
            print('\nMenu\n'
                  '======\n'
                  '1. Apply Leave\n'
                  '2. Cancel Leave\n'
                  '3. Display Employee Leave Profile\n'
                  '4. Daily Movement Update\n'
                  '5. Update Safe Management Measure Percentage\n'
                  "6. Display Departments' SMM status\n"
                  '0. Exit')
            choice = int(input("Enter option: "))
            print()
            if 0 <= choice <= 6:
                return choice
            else:
                raise ValueError
        except:    
            print('Please enter a valid selection number\n')

def inputDate(message) -> datetime:
    """ Validate and return user input in datetime """
    while True:
        try:
            userInput = input(message)
            return datetime.strptime(userInput, '%d/%M/%Y')
        except ValueError:
            print(f'{userInput} is not in the format dd/mm/yyyy')

def inputIntId(message) -> int:
    """ Validate and return user input in int """
    while True:
        try:
            userInput = input(message)
            return int(userInput)
        except ValueError:
            print(f'{userInput} is not a valid ID, please re-try')

def getEmployeeAndDept(companySUSS: Company, employeeId: int, dept: str) -> Union[Employee, Department]:
    employeeDept = companySUSS.searchDepartment(dept)
    if employeeDept == None:
        print('No matching department, please re-try')
        return None, None
    else:
        applicant = employeeDept.searchEmployee(employeeId)
        if applicant == None:
            print('No such employee, please re-try')
            return None, None
    return applicant, employeeDept

def applyLeave(companySUSS: Company, applicantId: int, dept: str) -> None:
    """ Adds Leave object to the company leaveApplication record """
    applicant, employeeDept = getEmployeeAndDept(companySUSS,applicantId,dept)
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
                if companySUSS.getVaccinationLeaveCount(applicantId, fromDate.year) >= 2:
                    raise LeaveApplicationException('Not allow to apply more than 2 vaccination leaves within same year') 
                newLeave = VaccinationLeave(applicant,fromDate,toDate)
            else:
                newLeave = Leave(applicant,fromDate,toDate)
            companySUSS.addLeave(newLeave)
            print(f'Leave Request Added!!\n{newLeave}')
        except LeaveApplicationException as e:
            print(e)
            
def cancelLeave(companySUSS: Company, employeeId: int, leaveId: int) -> None:
    """ Cancels an approved leave request based on employeeId and leaveRequestId """
    try:
        companySUSS.cancelLeave(employeeId,leaveId)
        print(f'Leave request {leaveId} cancelled successfully')
    except LeaveApplicationException as e:
        print(e)

def displayEmployeeLeaveProfile(companySUSS: Company, employeeId: int, dept: str) -> None:
    """ Displays all the employee's leave profile in the company """
    applicant, employeeDept = getEmployeeAndDept(companySUSS,employeeId,dept)
    if applicant != None and employeeDept != None:
        leaveList = companySUSS.getLeave(employeeId)
        print(applicant)
        if len(leaveList) == 0:
            print('Employee has no leave request record')
        else:
            for l in leaveList:
                print(l,end='\n\n')

def dailyMovementUpdate(companySUSS: Company, employeeId: int, dept:str) -> None:
    """ Shows the WFH status of an employee. Prompts if user want to change the status """
    applicant, employeeDept = getEmployeeAndDept(companySUSS,employeeId,dept)
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
        
def updateSMMPercentage(companySUSS : Company) -> None:
    """ Updates the Safe Management Measure (0% - 100%) """
    print(f'Current Safe Mangement Measure % is {companySUSS.getSafeManagePercentage():.1f}')
    
    while True:
        try:
            newPercentage = float(input('Enter new Safe Management Measure %: '))
            if 0 <= newPercentage <= 100: break
            else: raise ValueError
        except (UnboundLocalError, ValueError):
            print('Sorry, please re-enter withing range (0, 100)')

    companySUSS.setSafeManagePercentage(newPercentage)
    print(f'Safe Mangement Measure % updated to {newPercentage:.1f}')

def main() -> None:
    companySUSS = Company('SUSS', 'EDU1002334')
    insertData(companySUSS)
    
    while True:
        choice = menu()
        if   choice == 0: break
        elif choice == 1: applyLeave(companySUSS, inputIntId('Enter Employee ID: '), input("Enter employee's department: "))
        elif choice == 2: cancelLeave(companySUSS, inputIntId('Enter employee ID: '), inputIntId('Enter leave request ID to cancel: '))
        elif choice == 3: displayEmployeeLeaveProfile(companySUSS, inputIntId('Enter employee ID: '), input("Enter employee's department: "))
        elif choice == 4: dailyMovementUpdate(companySUSS, inputIntId('Enter employee ID: '), input("Enter employee's department: "))
        elif choice == 5: updateSMMPercentage(companySUSS)
        elif choice == 6: print(companySUSS)

if __name__ == '__main__':
    main()