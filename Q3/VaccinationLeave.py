from Leave import Leave, LeaveApplicationException
from Employee import Employee
from datetime import datetime, date

class VaccinationLeave(Leave):
    """ VaccinationLeave class is a subclass of Leave. """
    def __init__(self, applicant: Employee, fromDate: datetime, toDate: datetime) -> None:
        """ Creates a VaccinationLeave object with the given parameter and returns as a Leave object.

        Args:
            applicant (Employee): The Employee object that is applying for the leave.
            fromDate (datetime): The starting date of the leave.
            toDate (datetime): The end date of the leave.

        Raises:
            LeaveApplicationException: Leave request should not have from-date on weekend.
            LeaveApplicationException: Leave request from-Date is after to-Date.
            LeaveApplicationException: Applicant's leave balance is lesser than leave duration.
        
        Returns:
            VaccinationLeave: The VaccinationLeave object created with the given paramater.
        """
        super().__init__(applicant, fromDate, toDate)
        self._duration = 0            
    
    def __str__(self) -> str:
        """ 
        Returns:
            str: The content of the object. 
        """
        return f'Leave Request ID: {super().leaveRequestID}\n' \
               f'ID: {super().applicant.employeeId}\t\tName: {super().applicant.name}\n' \
               f'From: {super().fromDate.strftime("%d %b %y")} to {super().toDate.strftime("%d %b %y")}\n' \
               f'Duration: {super().duration} day (vacination)\n' \
               f'Status: {super().status}'