class Employee:
    def __init__(self, employeeId : int, name : str, workFromHome : bool) -> None:
        self._employeeId = employeeId
        self._name = name
        self._workFromHome = workFromHome
        self._leaveBalance = 0

    @property
    def employeeId(self) -> int: 
        return self._employeeId
    
    @property
    def name(self) -> str: 
        return self._name
    
    @property
    def workFromHome(self) -> bool: 
        return self._workFromHome
    @workFromHome.setter
    def workFromHome(self, atHome : bool) -> None: 
        self._workFromHome = atHome
        
    @property
    def leaveBalance(self) -> int:
        return self._leaveBalance
    
    def adjustLeave(self, adjustment: int) -> None:
        """ Adjusts the leave balance of the Employee object """
        self._leaveBalance += adjustment
    
    def __str__(self) -> str:
        return f'ID: {self._employeeId}\tName: {self._name}\tLeave Balance: {self._leaveBalance}\tWFH: {"Yes" if self._workFromHome else "No "}\t'