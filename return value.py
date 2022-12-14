import datetime as dt
class Member:
    def __init__(self,username,fullname):
        self.username = username
        self.fullname = fullname
        self.date_joined = dt.date.today()
        self.is_active = True
member_1 = Member("Ravi","Ravi Verma")

print(member_1.fullname)
print(member_1.date_joined)
print(member_1.is_active)
