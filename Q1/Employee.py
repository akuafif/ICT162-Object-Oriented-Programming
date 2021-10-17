from abc import ABC, abstractmethod

class Employee(ABC):
    """ Employee class is an abstract superclass that models one employee. """
    
    def __init__(self, employeeId: int, name: str, workFromHome: bool) -> None:
        """ Constructs all the necessary attributes for the Employee object. 

        Args:
            employeeId (int): unique id of the employee.
            name (str): name of the employee.
            workFromHome (bool): True is employee is working from home. False otherwise.
        """
        self.__employeeId = employeeId
        self.__name = name
        self.__workFromHome = workFromHome
        self.__leaveBalance = 0

    @property
    def employeeId(self) -> int: 
        """ Getter method for the employee's ID.

        Returns:
            int: id of the employee. 
        """
        return self.__employeeId
    
    @property
    def name(self) -> str: 
        """ Getter method for the employee's name.

        Returns:
            str: days of leave entitlement.
        """
        return self.__name
    
    @property
    def workFromHome(self) -> bool:
        """ Getter method for employee's work from home status.

        Returns:
            bool: True if employee is working from home. False otherwise. 
        """
        return self.__workFromHome 
        
    @workFromHome.setter
    def workFromHome(self, atHome: bool) -> None: 
        """ Setter method for employee workFromHome status.

        Args:
            atHome (bool): True is employee is working from home. False otherwise. 
        """
        self.__workFromHome = atHome
    
    @abstractmethod
    def getLeaveEntitlement(self) -> int:
        """ Returns the leave entitlement for employees.

        Returns:
            int: days of leave entitlement.
        """
        pass

    def adjustLeave(self, adjustment: int) -> None:
        """ Adjust the employee's leave balance.

        Args:
            adjustment (int): postive value to add, otherwise negative value to deduct. 
        """
        self.__leaveBalance += adjustment
    
    def __str__(self) -> str:
        """ 
        Returns:
            str: content of the object. 
        """
        return f'ID: {self.__employeeId}\tName: {self.__name}\tLeave Balance: {self.__leaveBalance}\tWFH: {"Yes" if self.__workFromHome else "No"}'