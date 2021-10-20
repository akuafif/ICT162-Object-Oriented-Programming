from Manager import Manager
from Employee import Employee

class Department:
    """ Department class is a class that models one department. """

    def __init__(self, name: str, manager: Employee, essentialServices: bool) -> None: 
        """ Constructs all the necessary attributes for the Department object. 

        Args:
            name (str): name of the department.
            manager (Employee): manager of the department.
            essentialServices (bool): True is department is an essential service. False otherwise.
        """
        self._name = name
        self._employees = []
        self._manager = manager
        self._essentialServices = essentialServices
        
    @property
    def name(self) -> str:
        """ Getter method for department name.

        Returns:
            str: name of the department.
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
            employeeId (int): id of the employee to search with.

        Returns:
            Employee: Employee object with the matching employeeId. Otherwise, None.
        """
        if self._manager.employeeId == employeeId:
            return self._manager
        for e in self._employees:
            if employeeId == e.employeeId:
                return e
        return None

    def addEmployee(self, newEmployee: Employee) -> bool:
        """ Adds an employee into the department. \n
        ONLY part-time and full-time employee is added to the department's employee list.

        Args:
            newEmployee (Employee): Employee object to be added into the department.

        Returns:
            bool: True if the operation is successfully, otherwise False.
        """
        if self.searchEmployee(newEmployee.employeeId) == None and type(newEmployee) != Manager:
            self._employees.append(newEmployee)
            return True
        return False
    
    def safeManagementCheck(self, percentage: float) -> str:
        """ Counts all the employees who are working from home and computes the percentage of employee working from home (include the manager).
        
        Args:
            percentage (float): value of safe management percentage to check with.

        Returns:
            str: report of all the employees who are WFH and computes the percentage of employee WFH (including the manager).
        """
        # Get the amount of employees working from home
        # True(bool) = 1(int). True + True = 2
        workFromHome = sum(e.workFromHome for e in self._employees if e.workFromHome)
                
        # Include the manager
        workFromHome += self._manager.workFromHome
        
        # Get percentage of employee working from home        
        deptPercentageWFH = workFromHome / (len(self._employees) + 1) * 100
        
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
            str: content of the object. 
        """
        printStr = f'Department {self._name}\tEssential Services: {"Yes" if self._essentialServices else "No"}' +\
                    f'\nManager {str(self._manager)}\n' +\
                    '\n'.join(str(e) for e in self._employees)
        return printStr