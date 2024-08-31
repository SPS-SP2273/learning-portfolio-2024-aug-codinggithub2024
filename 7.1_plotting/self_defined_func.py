def testing(one):
    return one**one

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return False
        else:
            return True
    return False
    
    
class Name(object):
    def __init__(self, name):
        self.name= name
        
