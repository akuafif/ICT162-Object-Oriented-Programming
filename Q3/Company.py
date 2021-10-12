from VaccinationLeave import VaccinationLeave
from Leave import Leave, LeaveApplicationException
from datetime import datetime
from Department import Department

class Company:
    """ A class to represent a company. """

    _SAFE_MANAGEMENT_PERCENTAGE = 50.0
    
    def __init__(self, name: str, uniqueEntityNumber: str) -> None:
        """ Constructs all the necessary attributes for the Company object. 

        Args:
            name (str): name of the company.
            uniqueEntityNumber (str): unique entity number of the company.
        """
        self._name = name
        self._uniqueEntityNumber = uniqueEntityNumber
        self._department = []
        self._leaveApplications = {} # Key:Value = employeeId : [Leave]
      
    @classmethod  
    def getSafeManagePercentage(cls) -> float:
        """ Return the Safe Management Percentage of the Company (Class variable).

        Returns:
            float: value of the current Safe Management Percentage.
        """
        return cls._SAFE_MANAGEMENT_PERCENTAGE
    
    @classmethod
    def setSafeManagePercentage(cls, newPercentage: float) -> None:
        """ Set the Safe Management Percentage for the Company (Class variable).

        Args:
            newPercentage (float): value of the new percentage.
        """
        cls._SAFE_MANAGEMENT_PERCENTAGE = newPercentage
        
    def searchDepartment(self, name: str) -> Department:
        """ Search for a Department object by name.

        Args:
            name (str): name of the department to search.

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
        if self.searchDepartment(newDepartment.name) == None:
            self._department.append(newDepartment)
            return True
        return False
    
    def getLeave(self, employeeId: int) -> list:
        """ Search all the leaves applied by employee ID.

        Args:
            employeeId (int): id of the employee to be search with.

        Returns:
            list: list of leave applied by the employee
        """
        # Returns empty list if employeeId not found in dictionary key
        return self._leaveApplications.get(employeeId, []) 
    
    def addLeave(self, leave: Leave) -> None:
        """ Adds a Leave object to the company records.

        Args:
            leave (Leave): Leave object to be added into the company records.

        Raises:
            LeaveApplicationException: if leave request overlaps with an approved leave.
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
        if leave.fromDate <= datetime.now() <= leave.toDate:
            leave.applicant.workFromHome = True
    
    def cancelLeave(self, employeeId: int, leaveRequestId: int) -> None:
        """ Cancels an employee's leave application.

        Args:
            employeeId (int): id of the employee of the Leave object
            leaveRequestId (int): leave request ID of the Leave object

        Raises:
            LeaveApplicationException: if there are no leave requests for this employee.
            LeaveApplicationException: if the leaveRequestId was not found for the employee.
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
            employeeId (int): id of the employee to be search with.
            fromDate (datetime): starting date of the search.
            toDate (datetime): end date of the search.

        Returns:
            bool: True if fromDate and toDate have any overlapping with existing leave request. False otherwise.
        """
        leaveList = self.getLeave(employeeId)
        for l in leaveList:
            if l.status == 'Approved':
                compareStart = max(l.fromDate, fromDate)
                compareEnd = min(l.toDate, toDate)     
                if ((compareEnd-compareStart).days + 1) > 0 :
                    return True
        return False
    
    def getVaccinationLeaveCount(self, employeeId: int, year: int) -> int:
        """ Get the total number of approved vaccination leave matching the employee ID for the given year.

        Args:
            employeeId (int): id of the employee to be search with.
            year (int): year to be search with.

        Returns:
            int: days of approved vaccination leaves.
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
            str: content of the object. 
        """
        printStr = f'Company: {self._name}\tUEN: {self._uniqueEntityNumber}'
        for dept in self._department:
            printStr += '\n' + str(dept) + '\n' + dept.safeManagementCheck(type(self)._SAFE_MANAGEMENT_PERCENTAGE)
        return printStr