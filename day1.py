from ast import increment_lineno
import sys

f = open(sys.argv[1], "r").read().split('\n')
# Solution for 1
increased = 0

for i in range(0, len(f)-1):
    if (f[i] < f[i+1]):
        increased+=1

print(increased)

# Solution for 2
sonar_increased = 0

for i in range(0, len(f)-3):
    if(f[i] < f[i+3]):
        sonar_increased+=1; 

print(sonar_increased)  
