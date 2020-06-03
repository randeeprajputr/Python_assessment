import os
import pandas as pd
from itertools import combinations

#taking advantage of pre-defined itertools library with of python
def findPairs(lst,s):
     return[pair for pair in combinations(lst,1) if sum(pair)==s] 


if __name__ == "__main__": 
#changing directory for locattion of dataset
    os.chdir("/home/randeep/Desktop/Internship assessment")
#creating dataframe from the input data    
    df=pd.read_csv("problem1.csv",delimiter=',')
#now convert it into list
    lst=[int(row) for row in df.values]
#take input of sum value value must be between -9990 to 9999
    s=int(input("Enter the sum value To find its Pairs"))
    if(s>=(-9990) and (s<=9999)):
        a=[int(row) for row in findPairs(lst,s)]
        if(a==[]):
            print("There is no pair exist")
        else:
            print(a)
        
    else:
        print("You Entered the sum value out of bound")
