"""
This is basically practicing some python ~
atm.py
contains atm class
"""
class atm:
    """
    initializes atm objcet. Can withdraw money
    """
    def __init__(self, bank_name, balance):
        self._balance = balance
        self._bank_name = bank_name
        print "atm for: ({}) initialized successfully with balance: ({}).\n".format(self._bank_name, self._balance)


    def withdraw(self, request):
        """
        prints banknote value returned by atm for a request if atm has money
        this works with INTGERS ONLY
        returns the rest of money in balance
        """
        # local variables
        accepted_notes = [100, 50, 10, 5, 1]
        # validating input
        if not type(request) == type(1):
            print "request must be an INTGER"
            return
        if not request < self._balance:
            print "atm doesn't have enough money"
            return

        print "============================"
        print "Welcome to {} atm".format(self._bank_name)
        print "Current balance:", self._balance
        print "Withdraw Value:", request
        print "============================"

        self._balance -= request
        # main loop
        for note in accepted_notes:
            while request >= note:
                request -= note
                print "give", note

        print "============================"
        print "balance after withdraw:", self._balance
        print "============================\n"
