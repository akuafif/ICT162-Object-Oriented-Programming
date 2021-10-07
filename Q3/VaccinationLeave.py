from Leave import Leave

class VaccinationLeave(Leave):
    """ VaccinationLeave class is a subclass of Leave. """
    
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