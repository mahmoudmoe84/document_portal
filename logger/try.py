import os 
import sys 


print(os.path.dirname(__file__))

print("==============")
print(os.path.abspath(__file__))

print("==============")
print(os.path.dirname(os.path.abspath(__file__)))