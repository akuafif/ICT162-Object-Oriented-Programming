from Employee import Employee

class PartTimeEmployee(Employee):
    """ PartTimeEmployee class is a subclass of Employee. """
    
    _LEAVE_ENTITLEMENT = {15:5, 30:10, 99:12}
    
    def __init__(self, employeeId: int, name: str, workFromHome: bool, hoursPerWeek: int) -> None:
        """ Create an PartTimeEmployee object with the given paramater and returns it.

        Args:
            employeeId (int): Employee's unique ID.
            name (str): Employee's name.
            workFromHome (bool): True is employee is working from home. False otherwise.
            hoursPerWeek (int): The amount of hours per week worked by the employee.
        
        Returns:
            PartTimeEmployee: The PartTimeEmployee object created with the given paramater.
        """
        super().__init__(employeeId,name,workFromHome)
        self._hoursPerWeek = hoursPerWeek
        super().adjustLeave(self.getLeaveEntitlement())
    
    def getLeaveEntitlement(self) -> int:
        """ Returns the starting leave balanace for part time employees.

        Returns:
            int: The starting leave balance.
        """
        for hrWorked, leave in type(self)._LEAVE_ENTITLEMENT.items():
            if self._hoursPerWeek <= hrWorked:
                return leave
        return 12
    
    def __str__(self) -> str:
        """ 
        Returns:
            str: The content of the object. 
        """
        return super().__str__() + f' Hours/Week: {self._hoursPerWeek}' 