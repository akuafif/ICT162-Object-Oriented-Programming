from Employee import Employee

class FullTimeEmployee(Employee):
    """ FullTimeEmployee class is a subclass of Employee. """
    
    _LEAVE_ENTITLEMENT = {4:22, 3:20, 2:18, 1:16, 0:16}
    
    def __init__(self, employeeId: int, name: str, workFromHome: bool, grade: int) -> None:
        """ Constructs all the necessary attributes for the FullTimeEmployee object.

        Args:
            employeeId (int): unique id of the employee.
            name (str): name of the employee.
            workFromHome (bool): True is employee is working from home. False otherwise.
            grade (int): employment grade of the employee.
        """
        super().__init__(employeeId, name, workFromHome)
        self.__grade = grade
        super().adjustLeave(self.getLeaveEntitlement())
        
    def getLeaveEntitlement(self) -> int:
        """ Returns the leave entitlement for full-time employees.

        Returns:
            int: days of leave entitlement.
        """
        for grade, leave in type(self)._LEAVE_ENTITLEMENT.items():
            if self.__grade == grade:
                return leave
    
    def __str__(self) -> str:
        """ 
        Returns:
            str: content of the object. 
        """
        return super().__str__() + f'\tGrade: {self.__grade}'