class Employee:
    def __init__(self, employeeId : int, name : str, workFromHome : bool) -> None:
        self._employeeId = employeeId
        self._name = name
        self._workFromHome = workFromHome
        self._leaveBalance = 0

    @property
    def employeeId(self) -> int: 
        """ Returns the employee ID"""
        return self._employeeId
    
    @property
    def name(self) -> str: 
        """ Returns the employee's name """
        return self._name
    
    @property
    def workFromHome(self) -> bool:
        """ Returns True if employee is working from home. False otherwise """ 
        return 'Yes' if self._workFromHome else 'No'
    @workFromHome.setter
    def workFromHome(self, atHome : bool) -> None: 
        """ Set the employee working from home """
        self._workFromHome = atHome
        
    @property
    def leaveBalance(self) -> int:
        """ Returns the employee's leave balance """
        return self._leaveBalance
    
    def adjustLeave(self, adjustment: int) -> None:
        """ Adjust the employee leave balance """
        self._leaveBalance += adjustment
    
    def __str__(self) -> str:
        return f'ID: {self._employeeId}\tName: {self._name}\tLeave Balance: {self._leaveBalance}\tWFH: {"Yes" if self._workFromHome else "No "}\t'