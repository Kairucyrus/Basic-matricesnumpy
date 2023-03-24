# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 22:45:37 2023

@author: Kairu Cyrus
"""

import numpy as np
m1 = np.array([[4, 10, 14], [9, 7, 11], [-8, 6, 18]])
m2 = np.array([[12,16,5],[13,8,19],[16,2,7]])

# addition 
m3 = m1+m2
print(m3) #returns [[16 26 19]
             #      [22 15 30]
             #      [ 8  8 25]]

#subtraction only differs from the addition by the oprator only, and maybe the result
m3 = m1- m2
print(m3)        #returns [[ -8  -6   9]
                 #         [ -4  -1  -8]
                #          [-24   4  11]]
#multiplication                
m3 = m1*m2
print(m3) # result: [[  48  160   70]
          #          [ 117   56  209]
          #          [-128   12  126]]
 
#Transpose
m4 = m1.transpose()            
print(m4)   #result: [[ 4  9 -8]
            #         [10  7  6]
            #         [14 11 18]]
#slice operations
print(m1[1:2, 0:2]) # keen on the way we write it
                    # The above will print the second row ([1]) (the third row is unincluded) and the first two columns of the row
                    # the left side(1:2) specifies the row(s) while the second part the column(s)
                    #result: [[9 7]]
#printing all rows;
print(m2[:, ])      # result: [[12 16  5]
                    #          [13  8 19]
                    #          [16  2  7]]
#printing the third column
print(m2[:, 2])     #[ 5 19 7]   
