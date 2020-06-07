class PersonInfo:
    def __init__(self):
        self.num_kids = 0

    # FIXME: Write inc_num_kids(self)

    ''' Your solution goes here '''
    def inc_num_kids(self):
        self.num_kids = self.num_kids + 1
        return self.num_kids

person1 = PersonInfo()

print('Kids:', person1.num_kids)
person1.inc_num_kids()
print('New baby, kids now:', person1.num_kids)