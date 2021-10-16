from Leave import Leave, Employee, datetime, LeaveApplicationException

class VaccinationLeave(Leave):
    """ VaccinationLeave class is a subclass of Leave. """
    def __init__(self, applicant: Employee, fromDate: datetime, toDate: datetime) -> None:
        """ Constructs all the necessary attributes for the VaccinationLeave object.

        Args:
            applicant (Employee): The Employee object that is applying for the leave.
            fromDate (datetime): The starting date of the leave.
            toDate (datetime): The end date of the leave.

        Raises:
            LeaveApplicationException: if from-Date is not same as to-Date
            LeaveApplicationException: if from-Date is before 30 Dec 2020
        """
        
        # Raise exception if both date are not the same
        if fromDate != toDate:
            raise LeaveApplicationException('From-date not the same as to-Date')
        
        # Raise exception if both date are before 30 Dec 2020
        if fromDate > datetime(year = 2020, month = 12, day = 30):
            raise LeaveApplicationException('Leave date is before 30 Dec 2020')
        
        # Use parent init to continue with constructor and to check for other exception
        super().__init__(applicant, fromDate, toDate)
    
    def __str__(self) -> str:
        """ 
        Returns:
            str: the content of the object. 
        """
        return f'Leave Request ID: {super().leaveRequestID}\n' \
               f'ID: {super().applicant.employeeId}\t\tName: {super().applicant.name}\n' \
               f'From: {super().fromDate.strftime("%d %b %y")} to {super().toDate.strftime("%d %b %y")}\n' \
               f'Duration: {super().duration} day (vacination)\n' \
               f'Status: {super().status}'