class Employee:

    def __init__(self, first, last, amount):
        self.first = first
        self.last = last
        self.amount = amount

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    