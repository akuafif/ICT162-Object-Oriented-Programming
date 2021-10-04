from Employee import Employee

class FullTimeEmployee(Employee):
    """ FullTimeEmployee class is a subclass of Employee. """
    
    _LEAVE_ENTITLEMENT = {4:22, 3:20, 2:18, 1:16, 0:16}
    
    def __init__(self, employeeId: int, name: str, workFromHome: bool, grade: int) -> None:
        """ Create an FullTimeEmployee object with the given paramater and returns it.

        Args:
            employeeId (int): Employee's unique ID.
            name (str): Employee's name.
            workFromHome (bool): True is employee is working from home. False otherwise.
            grade (int): Employment grade.
        
        Returns:
            FullTimeEmployee: The FullTimeEmployee object created with the given paramater.
        """
        super().__init__(employeeId, name, workFromHome)
        self._grade = grade
        super().adjustLeave(self.getLeaveEntitlement())
        
    def getLeaveEntitlement(self) -> int:
        for grade, leave in type(self)._LEAVE_ENTITLEMENT.items():
            if self._grade == grade:
                return leave
    
    def __str__(self) -> str:
        """ 
        Returns:
            str: The content of the object. 
        """
        return super().__str__() + f' Grade: {self._grade}'