from Leave import Leave, LeaveApplicationException
from Employee import Employee
from datetime import datetime, date

class VaccinationLeave(Leave):
    def __init__(self, applicant: Employee, fromDate: datetime, toDate: datetime) -> None:
        super().__init__(applicant, fromDate, toDate)
        self._duration = 0            
    
    def __str__(self) -> str:
        return f'Leave Request ID: {super().leaveRequestID}\n' \
               f'ID: {super().applicant.employeeId}\t\tName: {super().applicant.name}\n' \
               f'From: {super().fromDate.strftime("%d %b %y")} to {super().toDate.strftime("%d %b %y")}\n' \
               f'Duration: {super().duration} day (vacination)\n' \
               f'Status: {super().status}'