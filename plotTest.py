import matplotlib.pyplot as pl
#Importing the matplot module
'''
The code, attempts to draw a graphic of the wave, taking data from the 
output of test.py function.
draWave(0,5,7,10,8,6,2,-1,-3,-4)

'''
pl.plot([0,5,7,10,8,6,2,-1,-3,-4])
pl.ylabel('Values of test.py')
pl.xlabel('Numbers')
pl.show()
