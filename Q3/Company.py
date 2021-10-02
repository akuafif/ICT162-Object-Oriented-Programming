from VaccinationLeave import VaccinationLeave, Leave, LeaveApplicationException
from datetime import datetime
from Department import Department

class Company:
    _SAFE_MANAGEMENT_PERCENTAGE = 50.0
    
    def __init__(self, name: str, uniqueEntityNumber: str) -> None:
        self._name = name
        self._uniqueEntityNumber = uniqueEntityNumber
        self._department = []
        self._leaveApplications = {} # Key:Value = employeeId : [Leave]
      
    @classmethod  
    def getSafeManagePercentage(cls) -> float:
        """ Return the Safe Management Percentage """
        return cls._SAFE_MANAGEMENT_PERCENTAGE
    
    @classmethod
    def setSafeManagePercentage(cls, newPercentage: float) -> None:
        """ Set the Safe Management Percentage """
        cls._SAFE_MANAGEMENT_PERCENTAGE = newPercentage
        
    def searchDepartment(self, name: str) -> Department:
        """  Returns the  Department  object  with  the matching name.  If not found, it returns None. """
        for dept in self._department:
            if name == dept.name:
                return dept
        return None
        
    def addDepartment(self, newDepartment: Department) -> bool:
        """ Adds a new department into the _departments list if the department is not present in the list. 
        
        The method returns True if the department is added successfully, and False otherwise. """
        if self.searchDepartment(newDepartment) == None:
            self._department.append(newDepartment)
            return True
        return False
    
    def getLeave(self, employeeId: int) -> list:
        """ Returns a list of leave object for the given employeeId """
        return self._leaveApplications.get(employeeId, []) 
    
    def addLeave(self, leave: Leave) -> None:
        """ Adds a Leave object to the employee's leaveApplications list. Raise LeaveApplicationException if the given Leave object overlaps with any approved leave """
        # Compares for any approved leave overlap for the applicant
        if self.overlappingLeave(leave.applicant.employeeId, leave.fromDate, leave.toDate):
            del leave
            raise LeaveApplicationException('Leave application cannot overlaps with approved leave')
        
        # To add to employee's leave list, adjust leave and set WFH = True if the leave include today()
        if not self._leaveApplications.get(leave.applicant.employeeId, False):
            # initialise value with empty list if not yet created
            self._leaveApplications[leave.applicant.employeeId] = []
            
        self._leaveApplications[leave.applicant.employeeId].append(leave)
        leave.applicant.adjustLeave(leave.duration * -1)
        if leave.fromDate.date() <= datetime.now().date() <= leave.toDate.date():
            leave.applicant.workFromHome = True
    
    def cancelLeave(self, employeeId: int, leaveRequestId: int) -> None:
        """ Cancels an employee's leave application """
        leaveList = self.getLeave(employeeId)
        
        if len(leaveList) == 0:
            raise LeaveApplicationException(f'No leave requests for this employee {employeeId}')
        
        for leave in leaveList:
            if leave.leaveRequestID == leaveRequestId and leave.status == 'Approved':
                leave.status = 'Cancelled'
                leave.applicant.adjustLeave(leave.duration)
                break
        else:
            # if break not reached = no leave found
            raise LeaveApplicationException(f'Leave request {leaveRequestId} not found for this employee {employeeId}')
    
    def overlappingLeave(self, employeeId: int, fromDate: datetime, toDate: datetime) -> bool:
        """ Seaches the _leaveApplications for approved leave request for given employeeId.
        
        Returns True if fromDate and toDate have any overlapping with existing leave request. False otherwise"""
        leaveList = self.getLeave(employeeId)
        for l in leaveList:
            if l.status == 'Approved':
                compareStart = max(l.fromDate.date(), fromDate.date())
                compareEnd = min(l.toDate.date(), toDate.date())     
                if ((compareEnd-compareStart).days + 1) > 0 :
                    return True
        return False
    
    def getVaccinationLeaveCount(self, employeeId: int, year: int) -> int:
        """ Returns the number of apporved vaccination leaves matching the employeeId for that year """
        leaveList = self._leaveApplications.get(employeeId)
        vaccinationCount = 0
        if not len(leaveList) == 0:
            for leave in leaveList:
                if type(leave) == VaccinationLeave and leave.fromDate.year == year and leave.status == 'Approved':
                    vaccinationCount += 1
            return vaccinationCount
        return 0
    
    def __str__(self) -> str:
        printStr = f'Company: {self._name}\tUEN: {self._uniqueEntityNumber}'
        for dept in self._department:
            printStr += '\n' + str(dept) + '\n' + dept.safeManagementCheck(type(self)._SAFE_MANAGEMENT_PERCENTAGE)
        return printStr