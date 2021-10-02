class Employee:
    """ Employee class is an abstract superclass that models one employee. """
    
    def __init__(self, employeeId : int, name : str, workFromHome : bool) -> None:
        self._employeeId = employeeId
        self._name = name
        self._workFromHome = workFromHome
        self._leaveBalance = 0

    @property
    def employeeId(self) -> int: 
        """ Getter method for the employee's ID.

        Returns:
            int: The employee's ID. 
        """
        return self._employeeId
    
    @property
    def name(self) -> str: 
        """ Getter method for the employee's name.

        Returns:
            str: The employee's name. 
        """
        return self._name
    
    @property
    def workFromHome(self) -> bool:
        """ Getter method for employee's work from home status.

        Returns:
            bool: True if employee is working from home. False otherwise. 
        """
        return self._workFromHome 
        
    @workFromHome.setter
    def workFromHome(self, atHome : bool) -> None: 
        """ Setter method for employee workFromHome status.

        Args:
            atHome (bool): True is employee is working from home. False otherwise. 
        """
        self._workFromHome = atHome
        
    @property
    def leaveBalance(self) -> int:
        """ Getter method for employee's leave balance.

        Returns:
            int: The employee's leave balance.
        """
        return self._leaveBalance
    
    def adjustLeave(self, adjustment: int) -> None:
        """ Adjust the employee leave balance.

        Args:
            adjustment (int): Postive value to add. Otherwise, negative value to deduct. 
        """
        self._leaveBalance += adjustment
    
    def __str__(self) -> str:
        """ 
        Returns:
            str: The content of the object. 
        """
        return f'ID: {self._employeeId}\tName: {self._name}\tLeave Balance: {self._leaveBalance}\tWFH: {"Yes" if self._workFromHome else "No "}\t'