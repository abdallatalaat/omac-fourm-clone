"""
This is basically practicing some python ~
atm.py
contains function withdraw that prints the banknotes returned by atm
example: atm(500, 215) should return:
    give 100
    give 100
    give 10
    give 5
"""
def withdraw(money, request):
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
    if not type(money) == type(1):
        print "money must be an INTGER"
        return
    if not request < money:
        print "atm doesn't have enough money"
        return

    print "Current balance:", money

    # main loop
    for note in accepted_notes:
        while request >= note:
            request -= note
            print "give", note

    return money - request
