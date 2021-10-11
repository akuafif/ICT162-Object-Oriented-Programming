from imports.FullTimeEmployee import FullTimeEmployee

class Manager(FullTimeEmployee):   
    """ Manager class is a subclass of FullTimeEmployee. """
     
    _LEAVE_ENTITLEMENT = 25
        
    def getLeaveEntitlement(self) -> int:
        """ Returns the leave entitlement for manager object.

        Returns:
            int: The starting leave balance.
        """
        return type(self)._LEAVE_ENTITLEMENT