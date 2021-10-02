from Manager import Manager
from Employee import Employee

class Department:
    def __init__(self, name: str, manager: Manager, essentialServices: bool) -> None:
        self._name = name
        self._employees = []
        self._manager = manager
        self._essentialServices = essentialServices
        
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def essentialServices(self) -> bool:
        return self._essentialServices
    
    def searchEmployee(self, employeeId: int) -> Employee:
        """ Returns the Employee object with the matching employeeId. If not found, it returns None. """
        if self._manager.employeeId == employeeId:
            return self._manager
        for e in self._employees:
            if employeeId == e.employeeId:
                return e
        return None
    
    def addEmployee(self, newEmployee: Employee) -> bool:
        """ Accepts an Employee object as parameter and adds it into the _employees list if this employee is not present in the department. 
        
        Returns True if the employee is added successfully into the list and is not a Manager. False otherwise """
        if self.searchEmployee(newEmployee.employeeId) == None and type(newEmployee) != type(Manager):
            self._employees.append(newEmployee)
            return True
        return False
    
    def safeManagementCheck(self, percentage: float) -> str:
        """ This method counts all the employees who are WFH and computes the percentage of employee WFH (including the manager) """

        # Get the amount of employee working from home
        workFromHome = 0
        for e in self._employees:
            if e.workFromHome:
                workFromHome += 1
                
        # Include the manager
        workFromHome += 1 if self._manager.workFromHome else 0
        
        # Get percentage of employee working from home        
        deptPercentageWFH = (workFromHome / (len(self._employees) + 1) ) * 100
        
        # Checking for WFH requirement check
        if self._essentialServices:
            requirementCheck = 'exempted'
        elif deptPercentageWFH >= percentage:
            requirementCheck = 'passed requirement'
        else:
            requirementCheck = 'failed requirement'
        
        return f'No. of Employees working from home: {workFromHome} ({deptPercentageWFH:.1f}%) - {requirementCheck}.'
        
    def __str__(self) -> str:
        printStr = f'Department {self._name}\tEssential Services: {"Yes" if self._essentialServices else "No"}'
        printStr += '\n' + f'Manager ' + str(self._manager)
        for e in self._employees:
            printStr += '\n' + str(e)
        return printStr