from Manager import Manager
from Employee import Employee

class Department:
    """ Department class is an abstract superclass that models one department. """
    def __init__(self, name: str, manager: Manager, essentialServices: bool) -> None:
        self._name = name
        self._employees = []
        self._manager = manager
        self._essentialServices = essentialServices
        
    @property
    def name(self) -> str:
        """ Getter method for department name.

        Returns:
            str: The department name.
        """
        return self._name
    
    @property
    def essentialServices(self) -> bool:
        """ Getter method if department is a essential service department .

        Returns:
            bool: True if essential service. Otherwise, False.
        """
        return self._essentialServices
    
    def searchEmployee(self, employeeId: int) -> Employee:
        """ Search an employee by ID.

        Args:
            employeeId (int): The employee ID to search with.

        Returns:
            Employee: The Employee object with the matching employeeId. Otherwise, None.
        """
        for e in self._employees:
            if employeeId == e.employeeId:
                return e
        return None
    
    def addEmployee(self, newEmployee: Employee) -> bool:
        """ Adds an employee into the department. \n
        ONLY accepts part-time and full-time employee as the parameter.

        Args:
            newEmployee (Employee): The Employee object to be added into the department.

        Returns:
            bool: True if the operation is successfully, otherwise False.
        """
        if self.searchEmployee(newEmployee.employeeId) == None and type(newEmployee) != type(Manager):
            self._employees.append(newEmployee)
            return True
        return False
    
    def safeManagementCheck(self, percentage: float) -> str:
        """ 
        Args:
            percentage (float): The Safe Management Percentage to check with.

        Returns:
            str: The report of all the employees who are WFH and computes the percentage of employee WFH (including the manager).
        """
        # Get the amount of employee working from home
        workFromHome = 0
        for e in self._employees:
            if e.workFromHome == 'Yes':
                workFromHome += 1
                
        # Checks the manager if WFH
        workFromHome += 1 if self._manager.workFromHome == 'Yes' else 0
        
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
        """ 
        Returns:
            str: The content of the object. 
        """
        printStr = f'Department {self._name}\tEssential Services: {"Yes" if self._essentialServices else "No"}'
        printStr += '\n' + f'Manager ' + str(self._manager)
        for e in self._employees:
            printStr += '\n' + str(e)
        return printStr