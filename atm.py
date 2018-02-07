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
    prints the banknote value returned by atm for a certain request when atm has money
    """
    accepted_notes = [100, 50, 10, 5]
    assert request < money, "atm doesn't have enough money"
    for note in accepted_notes:
        while request >= note:
            request -= note
            print "give ", note



atm(400, 85)
