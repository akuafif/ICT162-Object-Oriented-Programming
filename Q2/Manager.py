from FullTimeEmployee import FullTimeEmployee

class Manager(FullTimeEmployee):    
    """ Manager class is a subclass of FullTimeEmployee. """
    
    _LEAVE_ENTITLEMENT = 25
    
    def __init__(self, employeeId: int, name: str, workFromHome: bool, grade: int) -> None:
        """ Create an Manager object with the given paramater and returns it.

        Args:
            employeeId (int): Employee's unique ID.
            name (str): Employee's name.
            workFromHome (bool): True is employee is working from home. False otherwise.
            grade (int): Employment grade.
        
        Returns:
            Manager: The Manager object created with the given paramater.
        """
        super().__init__(employeeId, name, workFromHome, grade)
        
    def getLeaveEntitlement(self) -> int:
        """ Returns the starting leave balanace for full-time managers.

        Returns:
            int: The starting leave balance.
        """
        return type(self)._LEAVE_ENTITLEMENT