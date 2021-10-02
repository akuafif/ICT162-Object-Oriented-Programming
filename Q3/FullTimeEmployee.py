from Employee import Employee

class FullTimeEmployee(Employee):
    
    _LEAVE_ENTITLEMENT = {4:22, 3:20, 2:18, 1:16, 0:16}
    
    def __init__(self, employeeId: int, name: str, workFromHome: bool, grade: int) -> None:
        super().__init__(employeeId, name, workFromHome)
        self._grade = grade
        super().adjustLeave(self.getLeaveEntitlement())
        
    def getLeaveEntitlement(self) -> int:
        for grade, leave in type(self)._LEAVE_ENTITLEMENT.items():
            if self._grade == grade:
                return leave
        return 16
    
    def __str__(self) -> str:
        return super().__str__() + f' Grade: {self._grade}'