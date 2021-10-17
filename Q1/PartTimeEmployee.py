from Employee import Employee

class PartTimeEmployee(Employee):
    """ PartTimeEmployee class is a subclass of Employee. """
    
    _LEAVE_ENTITLEMENT = {15:5, 30:10, 99:12}
    
    def __init__(self, employeeId: int, name: str, workFromHome: bool, hoursPerWeek: int) -> None:
        """ Constructs all the necessary attributes for the PartTimeEmployee object.

        Args:
            employeeId (int): unique id of the employee.
            name (str): name of the employee.
            workFromHome (bool): True is employee is working from home. False otherwise.
            hoursPerWeek (int): hours per week worked by the employee.
        """
        super().__init__(employeeId,name,workFromHome)
        self.__hoursPerWeek = hoursPerWeek
        super().adjustLeave(self.getLeaveEntitlement())
    
    def getLeaveEntitlement(self) -> int:
        """ Returns the leave entitlement for part time employees.

        Returns:
            int: days of leave entitlement.
        """
        for hrWorked, leave in type(self)._LEAVE_ENTITLEMENT.items():
            if self.__hoursPerWeek <= hrWorked:
                return leave
    
    def __str__(self) -> str:
        """ 
        Returns:
            str: content of the object. 
        """
        return super().__str__() + f'\tHours/Week: {self.__hoursPerWeek}' 