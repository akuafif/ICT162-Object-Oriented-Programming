from FullTimeEmployee import FullTimeEmployee

class Manager(FullTimeEmployee):    
    _LEAVE_ENTITLEMENT = 25
    
    def __init__(self, employeeId: int, name: str, workFromHome: bool, grade: int) -> None:
        super().__init__(employeeId, name, workFromHome, grade)
        
    def getLeaveEntitlement(self) -> int:
        """ Returns the starting leave balance for managers """
        return type(self)._LEAVE_ENTITLEMENT