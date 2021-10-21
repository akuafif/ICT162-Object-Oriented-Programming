from Employee import Employee
from datetime import datetime, timedelta

class Leave:
    """ Leave class is a class that models one Leave. """
    
    _NEXT_ID = 202100001
    
    def __init__(self, applicant: Employee, fromDate: datetime, toDate: datetime) -> None:
        """ Constructs all the necessary attributes for the Leave object.

        Args:
            applicant (Employee): Employee object that is applying for the leave.
            fromDate (datetime): starting date of the leave.
            toDate (datetime): end date of the leave.

        Raises:
            LeaveApplicationException: If leave request from-Date falls on weekend.
            LeaveApplicationException: If leave request from-Date is after to-Date.
            LeaveApplicationException: If applicant's leave balance is lesser than leave duration.
        """
        self._applicant = applicant
        self._fromDate = fromDate
        self._toDate = toDate
        
        # raise exception if fromDate is on weekend
        if self._fromDate.weekday() in [5,6]:
            raise LeaveApplicationException('Leave request should not have from-Date on weekend')
        
        # raise exception if from-Date is before, or same as to-Date
        if self._fromDate > self._toDate:
            raise LeaveApplicationException('Leave request from-Date is after to-Date')
        
        # get the amount of days between the fromDate and the toDate
        daysApart = (self._toDate - self._fromDate).days + 1
        
        # To get the amount of weekdays between fromDate and toDate
        # counts the length of list returned by the for loop containing weekdays dates, [datetime(2021,12,31), etc]
        # an outer for loop starts from fromDate, enumerate the list of timedelta returned by the nested loop, [timedelta(days=1),timedelta(days=2)..etc]
        # a nested for loop will create a list of timedelta objects in range of daysApart(int), for the outer loop to enumerate
        self._duration = len([dt.weekday() for dt in (self._fromDate + timedelta(days) for days in range(daysApart)) if not dt.weekday() in [5,6]])

        # raise exception if there is not enough leaveBalance for the leave duration
        if self._applicant.leaveBalance - self._duration < 0:
            raise LeaveApplicationException("Applicant's leave balance is lesser than leave duration")

        self._status = 'Approved'
        self._leaveRequestId = Leave._NEXT_ID
        
        # Using Leave._NEXT_ID allows child class to increment the value, instead of type(self)
        Leave._NEXT_ID += 1
        
    @property
    def leaveRequestID(self) -> int:
        """ Getter method for the leave request ID.

        Returns:
            int: leave request ID.
        """
        return self._leaveRequestId
    
    @property
    def applicant(self) -> Employee:
        """ Getter method for the applicant.

        Returns:
            Employee: applicant in Employee object
        """
        return self._applicant
    
    @property
    def fromDate(self) -> datetime:
        """ Getter method for the starting date of the leave.

        Returns:
            datetime: starting date of the leave.
        """
        return self._fromDate
    
    @property
    def toDate(self) -> datetime:
        """ Getter method for the end date of the leave.

        Returns:
            datetime: end date of the leave.
        """
        return self._toDate
    
    @property
    def duration(self) -> int:
        """ Getter method for the leave duration in days.

        Returns:
            int: amount of days for the leave duration.
        """
        return self._duration
    
    @property
    def status(self) -> str:
        """ Getter method for the leave status.

        Returns:
            str: leave status.
        """
        return self._status
    
    @status.setter
    def status(self, newStatus: str) -> None:
        """ Setter method for the leave status.

        Args:
            newStatus (str): new status of the leave.
        """
        self._status = newStatus
        
    def __str__(self) -> str:
        """ 
        Returns:
            str: content of the object. 
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