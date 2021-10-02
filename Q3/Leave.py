from Employee import Employee
from datetime import datetime, timedelta

class Leave:
    _NEXT_ID = 202100001
    
    def __init__(self, applicant: Employee, fromDate: datetime, toDate: datetime) -> None:
        self._leaveRequestId = type(self)._NEXT_ID
        type(self)._NEXT_ID += 1
        
        self._applicant = applicant
        self._fromDate = fromDate
        self._toDate = toDate
        self._duration = 0
        
        # raise exception if fromDate is on weekend or/and is after toDate
        if self._fromDate.strftime('%A') == 'Saturday' or \
            self._fromDate.strftime('%A') == 'Sunday':
            raise LeaveApplicationException('Leave request should not have from-date on weekend')
        if self._fromDate.date() > self._toDate.date():
            raise LeaveApplicationException('Leave request from-Date is after to-Date')
        
        # - compute duration by using fromDate and toDate
        # - if duration days is lesser than the leave balance, throw exception
        # - set status to approved  
        dateRange = (self._toDate.date() - self._fromDate.date()).days + 1
        for dt in (self._fromDate.date() + timedelta(n) for n in range(dateRange)):
            if not dt.weekday() in [5,6]:
                self._duration += 1

        if self._applicant.leaveBalance - self._duration < 0:
            raise LeaveApplicationException('Applicant leave balance is lesser than leave duration')
        self._status = 'Approved'
        
    @property
    def leaveRequestID(self) -> int:
        return self._leaveRequestId
    
    @property
    def applicant(self) -> Employee:
        return self._applicant
    
    @property
    def fromDate(self) -> datetime:
        return self._fromDate
    
    @property
    def toDate(self) -> datetime:
        return self._toDate
    
    @property
    def duration(self) -> int:
        return self._duration
    
    @property
    def status(self) -> str:
        return self._status
    
    @status.setter
    def status(self, newStatus) -> None:
        self._status = newStatus
        
    def __str__(self) -> str:
        return f'Leave Request ID: {self._leaveRequestId}\n' \
               f'ID: {self._applicant.employeeId}\t\tName: {self._applicant.name}\n' \
               f'From: {self._fromDate.strftime("%d %b %y")} to {self._toDate.strftime("%d %b %y")}\n' \
               f'Duration: {self._duration} days\n' \
               f'Status: {self._status}'

class LeaveApplicationException(Exception):
    pass