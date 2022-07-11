class Person(object):
    """Template for people"""
    
    # Class-level variable
    peopleCount = 0

    # Initializer (with implicit call to __new__)
    def __init__(self, name):
        self.name = name
        Person.peopleCount += 1
    
    # Equivalent of toString() 
    def __str__(self):
        return "str: " + self.name

    # Be unambiguous - reproduce the item. 
    # Possibly used with eval()
    # If __repr__ is overridden, it can be used for __str__
    # So if you have to do one, override __repr__
    def __repr__(self):
        return "repr: " + self.name

    def getCount(self):
        return Person.peopleCount

    def displayCount(self):
        print("Total people created: " + str(Person.peopleCount))
    