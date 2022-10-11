"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name
        self.EmployeeContract=""

    def get_pay(self):
        totalPay=0
        if self.EmployeeContract.hours:
            totalPay+=self.EmployeeContract.hours*self.EmployeeContract.hourRate
        if self.EmployeeContract.salary:
            totalPay+=self.EmployeeContract.salary
        if self.EmployeeContract.comissionNo:
            totalPay+=self.EmployeeContract.comissionNo*self.EmployeeContract.comissionPay
        return totalPay
    def __str__(self):
        explanation=f"{self.name} works on a "
        addAnd = False
        if self.EmployeeContract.salary:
            explanation+=f"monthly salary of {self.EmployeeContract.salary}"
            addAnd=True
        if self.EmployeeContract.hours:
            explanation+=f"contract of {self.EmployeeContract.hours} hours at {self.EmployeeContract.hourRate}/hour"
            addAnd=True
        if self.EmployeeContract.comissionNo:
            if addAnd:
                explanation+=" and receives "
            if self.EmployeeContract.comissionNo>1:
                explanation +=f"a comission for {self.EmployeeContract.comissionNo} contract(s) at {self.EmployeeContract.comissionPay}/contract"
            else:
                explanation +=f"a bonus comission of {self.EmployeeContract.comissionPay}"
        explanation+=f". Their total pay is {self.get_pay()}."
        return explanation
class EmployeeContract:
    def __init__(self, hours="",hourRate="",comissionNo="",comissionPay="",salary=""):
        self.hours=hours
        self.hourRate=hourRate
        self.comissionNo=comissionNo
        self.comissionPay=comissionPay
        self.salary=salary
# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')
billie.EmployeeContract=EmployeeContract(salary=4000)
# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')
charlie.EmployeeContract=EmployeeContract(hours=100,hourRate=25)
# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')
renee.EmployeeContract=EmployeeContract(salary=3000,comissionNo=4,comissionPay=200)
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')
jan.EmployeeContract=EmployeeContract(hours=150,hourRate=25,comissionNo=3,comissionPay=220)
# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')
robbie.EmployeeContract=EmployeeContract(salary=2000,comissionNo=1,comissionPay=1500)
# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
ariel.EmployeeContract=EmployeeContract(hours=120,hourRate=30,comissionNo=1,comissionPay=600)
