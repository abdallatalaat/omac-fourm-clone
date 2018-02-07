"""
This is basically practicing some python ~
atm.py
contains function atm that prints the banknotes returned by atm
example: atm(500, 215) should return:
    give 100
    give 100
    give 10
    give 5
"""
def atm(money, request):
    """
    prints banknote value returned by atm for a request if atm has money
    this works with INTGERS ONLY
    """
    # local variables
    accepted_notes = [100, 50, 10, 5, 1]

    # asserts
    assert request < money, "atm doesn't have enough money"
    assert type(request) == type(1), "request must be an INTGER"

    # main loop
    for note in accepted_notes:
        while request >= note:
            request -= note
            print "give", note



atm(400, 86)
