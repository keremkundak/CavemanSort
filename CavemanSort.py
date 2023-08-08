#CavemanSort is an esoteric sorting algorithm

#Pseudo code:
#1-List input
#2-If the list is sorted return
#3-If not sorted shuffle the list and go to step 2

import random
import time
import copy

def CavemanSort(x):
    #creating a deepcopy of the list so random.shuffle() does not affect the original list
    temp1 = copy.deepcopy(x)
    
    start = time.time()
    while(x != sorted(x)):
        random.shuffle(x)
    end = time.time()
    t = end-start
    print('The list before sorting: %s\nThe list after sorting: %s\nComputing time : %.3f'%(str(temp1),str(x), t))
    return None

#Test function creates 11 lists with len 1-11 to compare computing times
#Cannot test bigger lists because of the computing time gets ridiculuously long after length of 12
def Test():
    for i in range(1,12):
        randomList = random.sample(range(1,i+1),int(i))
        print(str(i)+'. list')
        CavemanSort(randomList)
    return None

Test()