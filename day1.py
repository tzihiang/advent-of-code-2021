import sys

with open(sys.argv[1]) as f:
    items = [int(line.strip()) for line in f]

# Solution for 1
increased=0

for i in range(0, len(items)-1):
    if (items[i] < items[i+1]):
        increased+=1

print(increased)

# Solution for 2
sonar_increased = 0

for i in range(0, len(items)-3):
    if(items[i] < items[i+3]):
        sonar_increased+=1; 

print(sonar_increased)  

