# Consider the following scenario where the UAV receives temperature data from the installed
# sensors in a residential area. Assume that there are nine sensors installed that are measuring
# temperature in centigrade. Develop a Python code to calculate the average temperature in F.

import numpy as np
import random

temp=[]

for i in range(9):
    temp.append(random.uniform(-2, 45))

temp=np.array(temp)

print("Temperature in Celsius: ",temp,"\n")

temp=temp*1.8+32

print("Temperature in Fahrenheit: ",temp,"\n")

print("Average: ",sum(temp)/9)
