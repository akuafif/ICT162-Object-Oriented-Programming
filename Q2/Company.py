from Department import Department

class Company:
    """ Company class is an abstract superclass that models one company. """
    
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
        if self.searchDepartment(newDepartment) == None:
            self._department.append(newDepartment)
            return True
        return False
    
    def __str__(self) -> str:
        """ 
        Returns:
            str: content of the object. 
        """
        printStr = f'Company: {self._name}\tUEN: {self._uniqueEntityNumber}'
        for dept in self._department:
            printStr += '\n' + str(dept) + '\n' + dept.safeManagementCheck(type(self)._SAFE_MANAGEMENT_PERCENTAGE)
        return printStr  