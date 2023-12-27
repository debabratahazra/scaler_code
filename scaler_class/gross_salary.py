'''
Take an integer A as input denoting the basic salary of an employee, you have to calculate the gross salary (in Rs.) with the help of the below conditions:

If A <= Rs 10,000 then HRA = 20%, DA = 80%
If A is between Rs 10,001 to Rs 20,000 then HRA = 25%, DA = 90%
If A >= Rs 20,001 then HRA = 30%, DA = 95%
For a given basic salary(BS or A), HRA and DA, Gross Salary is given by:

Gross Salary = BS + HRA + DA 
'''
import math

bs = int(input())
if bs <= 10000:
    hra = bs * 20/100
    da = bs * 80/100
elif bs > 10000 and bs <= 20000:
    hra = bs * 25/100
    da = bs * 90/100
else:
    hra = bs * 30/100
    da = bs * 95/100

gross = bs + hra + da
print(math.floor(gross))
