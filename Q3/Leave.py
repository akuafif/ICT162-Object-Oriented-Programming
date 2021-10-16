from Employee import Employee
from datetime import datetime, timedelta

class Leave:
    """ A class to represent a leave request. """
    
    _NEXT_ID = 202100001
    
    def __init__(self, applicant: Employee, fromDate: datetime, toDate: datetime) -> None:
        """ Constructs all the necessary attributes for the Leave object.

        Args:
            applicant (Employee): The Employee object that is applying for the leave.
            fromDate (datetime): The starting date of the leave.
            toDate (datetime): The end date of the leave.

        Raises:
            LeaveApplicationException: If leave request from-Date falls on weekend.
            LeaveApplicationException: If leave request from-Date is after to-Date.
            LeaveApplicationException: If applicant's leave balance is lesser than leave duration.
        """
        
        self.__applicant = applicant
        self.__fromDate = fromDate
        self.__toDate = toDate
        
        # raise exception if fromDate is on weekend
        if self.__fromDate.strftime('%A') == 'Saturday' or self.__fromDate.strftime('%A') == 'Sunday':
            raise LeaveApplicationException('Leave request should not have from-Date on weekend')
        
        # raise exception if from-Date is after to-Date
        if self.__fromDate > self.__toDate:
            raise LeaveApplicationException('Leave request from-Date is after to-Date')
        
        # get the amount of days between the fromDate and the toDate
        daysApart = (self.__toDate - self.__fromDate).days + 1
        
        # To get the amount of weekdays between fromDate and toDate
        # for loop from fromDate, enumerate the list of timedelta returned by the nested loop
        # nested for loop to create a list of timedelta(days) in range of daysApart(int) and return them 
        self._duration = len([dt.weekday() for dt in (self.__fromDate + timedelta(days) for days in range(daysApart)) if not dt.weekday() in [5,6]])

        # raise exception if there is not enough leaveBalance for the leave duration
        if self.__applicant.leaveBalance - self._duration < 0:
            raise LeaveApplicationException("Applicant's leave balance is lesser than leave duration")

        self._status = 'Approved'
           
        # _NEXT_ID increment after approved
        self.__leaveRequestId = type(self)._NEXT_ID
        type(self)._NEXT_ID += 1
        
    @property
    def leaveRequestID(self) -> int:
        """ Getter method for the leave request ID.

        Returns:
            int: The leave request ID.
        """
        return self.__leaveRequestId
    
    @property
    def applicant(self) -> Employee:
        """ Getter method for the applicant.

        Returns:
            Employee: Applicant in Employee object
        """
        return self.__applicant
    
    @property
    def fromDate(self) -> datetime:
        """ Getter method for the starting date of the leave.

        Returns:
            datetime: The starting date of the leave.
        """
        return self.__fromDate
    
    @property
    def toDate(self) -> datetime:
        """ Getter method for the end date of the leave.

        Returns:
            datetime: The end date of the leave.
        """
        return self.__toDate
    
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
        return f'Leave Request ID: {self.__leaveRequestId}\n' \
               f'ID: {self.__applicant.employeeId}\t\tName: {self.__applicant.name}\n' \
               f'From: {self.__fromDate.strftime("%d %b %y")} to {self.__toDate.strftime("%d %b %y")}\n' \
               f'Duration: {self._duration} days\n' \
               f'Status: {self._status}'

class LeaveApplicationException(Exception):
    """ LeaveApplicationException is a subclass of the Exception class. 
    
        This class has no additional attribute or method. When the application encounters a business rule violation, an exception from this class is raised"""
    pass