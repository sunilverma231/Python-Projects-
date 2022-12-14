import datetime as dt

class Member:
    free_day = 0
    def __init__(self,username, fullname):
        self.datejoined = dt.date.today()
        self.free_expires = dt.datetime.today() + dt.timedelta(Member.free_day)
        @classmethod
        def setfreedays(cls,days):
            cls.free_days = days
        @staticmethod
        def currenttime():
            nnow = dt.datetime.now()
            return f"{now:%I:%M%P}"
print(Member.currentime())