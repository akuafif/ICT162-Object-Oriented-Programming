from VaccinationLeave import VaccinationLeave, Leave, LeaveApplicationException
from datetime import datetime
from Department import Department

class Company:
    """ Company class is an abstract superclass that models one company. """

    _SAFE_MANAGEMENT_PERCENTAGE = 50.0
    
    def __init__(self, name: str, uniqueEntityNumber: str) -> None:
        """ Create an Company object with the given paramater and returns it.

        Args:
            name (str): The company name.
            uniqueEntityNumber (str): The unique entity number of the company.
              
        Returns:
            Company: The Company object created with the given paramater.
        """
        self._name = name
        self._uniqueEntityNumber = uniqueEntityNumber
        self._department = []
        self._leaveApplications = {} # Key:Value = employeeId : [Leave]
      
    @classmethod  
    def getSafeManagePercentage(cls) -> float:
        """ Return the Safe Management Percentage of the Company (Class variable).

        Returns:
            float: Value of the current Safe Management Percentage.
        """
        return cls._SAFE_MANAGEMENT_PERCENTAGE
    
    @classmethod
    def setSafeManagePercentage(cls, newPercentage: float) -> None:
        """ Set the Safe Management Percentage for the Company (Class variable).

        Args:
            newPercentage (float): Value of the new percentage.
        """
        cls._SAFE_MANAGEMENT_PERCENTAGE = newPercentage
        
    def searchDepartment(self, name: str) -> Department:
        """ Search for a Department object by name.

        Args:
            name (str): Department name to search.

        Returns:
            Department: Department object with the matching name. Otherwise, return None.
        """
        for dept in self._department:
            if name == dept.name:
                return dept
        return None
        
    def addDepartment(self, newDepartment: Department) -> bool:
        """ Adds a new department into the Company object.

        Args:
            newDepartment (Department): Department object to be added to the Company object.

        Returns:
            bool: True if the department is added successfully, and False otherwise.
        """
        if self.searchDepartment(newDepartment) == None:
            self._department.append(newDepartment)
            return True
        return False
    
    def getLeave(self, employeeId: int) -> list:
        """ Search all the leaves applied by employee ID.

        Args:
            employeeId (int): The employee's ID to be search with.

        Returns:
            list: List of leave applied by the employee
        """
        return self._leaveApplications.get(employeeId, []) 
    
    def addLeave(self, leave: Leave) -> None:
        """ Adds a Leave object to the company records.

        Args:
            leave (Leave): The Leave object to be added into the company records.

        Raises:
            LeaveApplicationException: Leave application cannot overlaps with approved leave.
        """
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
        """ Cancels an employee's leave application.

        Args:
            employeeId (int): The employee's ID of the Leave object
            leaveRequestId (int): The leave request ID of the Leave object

        Raises:
            LeaveApplicationException: No leave requests for this employee
            LeaveApplicationException: Leave request {leaveRequestId} not found for this employee {employeeId}
        """
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
        """ Search the company records for any overlapping leave requests for the given employee ID.

        Args:
            employeeId (int): The employee's ID to be search with.
            fromDate (datetime): The starting date of the search.
            toDate (datetime): The end date of the search.

        Returns:
            bool: True if fromDate and toDate have any overlapping with existing leave request. False otherwise.
        """
        leaveList = self.getLeave(employeeId)
        for l in leaveList:
            if l.status == 'Approved':
                compareStart = max(l.fromDate.date(), fromDate.date())
                compareEnd = min(l.toDate.date(), toDate.date())     
                if ((compareEnd-compareStart).days + 1) > 0 :
                    return True
        return False
    
    def getVaccinationLeaveCount(self, employeeId: int, year: int) -> int:
        """ Get the total number of approved vaccination leave matching the employee ID for the given year.

        Args:
            employeeId (int): The employee's ID to be search with.
            year (int): The year to be search with.

        Returns:
            int: Days of approved vaccination leaves.
        """
        leaveList = self._leaveApplications.get(employeeId)
        vaccinationCount = 0
        if not len(leaveList) == 0:
            for leave in leaveList:
                if type(leave) == VaccinationLeave and leave.fromDate.year == year and leave.status == 'Approved':
                    vaccinationCount += 1
            return vaccinationCount
        return 0
    
    def __str__(self) -> str:
        """ 
        Returns:
            str: The content of the object. 
        """
        printStr = f'Company: {self._name}\tUEN: {self._uniqueEntityNumber}'
        for dept in self._department:
            printStr += '\n' + str(dept) + '\n' + dept.safeManagementCheck(type(self)._SAFE_MANAGEMENT_PERCENTAGE)
        return printStr