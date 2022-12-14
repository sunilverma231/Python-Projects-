class Employee:
    no_of_leaves = 8
    def __init__(self,aname, asalary, arole):
        self.aname = aname
        self.asalary = asalary
        self.arole = arole
    def printdetails(self):
        return f"The name is {self.aname}. Salary is {self.asalary} and role is {self.arole}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

harrry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
#harrry.change_leaves(34)
rohan.change_leaves(84)

print(harrry.printdetails())
#print(harrry.no_of_leaves)
print(rohan.no_of_leaves)