from Employee import Employee
from datetime import datetime, timedelta

class Leave:
    """ A class to represent a leave request. """
    
    _NEXT_ID = 202100001
    
    def __init__(self, applicant: Employee, fromDate: datetime, toDate: datetime) -> None:
        """ Creates a Leave object with the given parameter and returns as a Leave object.

        Args:
            applicant (Employee): The Employee object that is applying for the leave.
            fromDate (datetime): The starting date of the leave.
            toDate (datetime): The end date of the leave.

        Raises:
            LeaveApplicationException: If leave request from-date falls on weekend.
            LeaveApplicationException: If leave request from-Date is after to-Date.
            LeaveApplicationException: If applicant's leave balance is lesser than leave duration.
        
        Returns:
            Leave: The Leave object created with the given paramater.
        """
        
        self._applicant = applicant
        self._fromDate = fromDate
        self._toDate = toDate
        
        # raise exception if fromDate is on weekend
        if self._fromDate.strftime('%A') == 'Saturday' or self._fromDate.strftime('%A') == 'Sunday':
            raise LeaveApplicationException('Leave request should not have from-date on weekend')
        
        # raise exception if from-Date is after to-Date
        if self._fromDate > self._toDate:
            raise LeaveApplicationException('Leave request from-Date is after to-Date')
        
        # get the amount of days between the fromDate and the toDate
        daysApart = (self._toDate - self._fromDate).days + 1
        
        # for loop to check the amount of weekdays between fromDate till daysApart, nested for loop the increment the timedelta(days) in range of daysApart
        self._duration = len([dt.weekday() for dt in (self._fromDate + timedelta(days) for days in range(daysApart)) if not dt.weekday() in [5,6]])

        # raise exception if there is not enough leaveBalance for the leave duration
        if self._applicant.leaveBalance - self._duration < 0:
            raise LeaveApplicationException("Applicant's leave balance is lesser than leave duration")

        self._status = 'Approved'
           
        # _NEXT_ID logic for YYYY99999 generator, for year other than 2021
        self._leaveRequestId = int(str(datetime.now().year) + str(type(self)._NEXT_ID)[4:])     
        type(self)._NEXT_ID = self._leaveRequestId + 1
        
    @property
    def leaveRequestID(self) -> int:
        """ Getter method for the leave request ID.

        Returns:
            int: The leave request ID.
        """
        return self._leaveRequestId
    
    @property
    def applicant(self) -> Employee:
        """ Getter method for the applicant.

        Returns:
            Employee: Applicant in Employee object
        """
        return self._applicant
    
    @property
    def fromDate(self) -> datetime:
        """ Getter method for the starting date of the leave.

        Returns:
            datetime: The starting date of the leave.
        """
        return self._fromDate
    
    @property
    def toDate(self) -> datetime:
        """ Getter method for the end date of the leave.

        Returns:
            datetime: The end date of the leave.
        """
        return self._toDate
    
    @property
    def duration(self) -> int:
        """ Getter method for the leave duration in days.

        Returns:
            int: The amount of days for the leave duration.
        """
        return self._duration
    
    @property
    def status(self) -> str:
        """ Getter method for the leave status.

        Returns:
            str: The leave status.
        """
        return self._status
    
    @status.setter
    def status(self, newStatus: str) -> None:
        """ Setter method for the leave status.

        Args:
            newStatus (str): The new status of the leave.
        """
        self._status = newStatus
        
    def __str__(self) -> str:
        """ 
        Returns:
            str: The content of the object. 
        """
        return f'Leave Request ID: {self._leaveRequestId}\n' \
               f'ID: {self._applicant.employeeId}\t\tName: {self._applicant.name}\n' \
               f'From: {self._fromDate.strftime("%d %b %y")} to {self._toDate.strftime("%d %b %y")}\n' \
               f'Duration: {self._duration} days\n' \
               f'Status: {self._status}'

class LeaveApplicationException(Exception):
    """ LeaveApplicationException is a subclass of the Exception class. 
    
        This class has no additional attribute or method. When the application encounters a business rule violation, an exception from this class is raised"""
    pass