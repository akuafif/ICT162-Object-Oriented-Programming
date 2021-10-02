from Employee import Employee

class PartTimeEmployee(Employee):
    """ PartTimeEmployee class is a subclass of Employee """
    
    _LEAVE_ENTITLEMENT = {15:5, 30:10, 99:12}
    
    def __init__(self, employeeId: int, name: str, workFromHome: bool, hoursPerWeek: int) -> None:
        super().__init__(employeeId,name,workFromHome)
        self._hoursPerWeek = hoursPerWeek
        super().adjustLeave(self.getLeaveEntitlement())
    
    def getLeaveEntitlement(self) -> int:
        """ Returns the starting leave balanace for part time employees in int. """
        for hrWorked, leave in type(self)._LEAVE_ENTITLEMENT.items():
            if self._hoursPerWeek <= hrWorked:
                return leave
        return 12
    
    def __str__(self) -> str:
        """ Returns the content of the object in readable string. """
        return super().__str__() + f' Hours/Week: {self._hoursPerWeek}' 