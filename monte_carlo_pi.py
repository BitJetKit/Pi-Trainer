# Author: Bit Jet Kit
# Title: monte_carlo_pi
# Date: August 29, 2021
# Purpose: Python implementation of Monte Carlo Pi Simulation
# Original Python Pi algorithm: Geeks for Geeks: https://www.geeksforgeeks.org/estimating-value-pi-using-monte-carlo/
import random, pyodbc 


# Use historical Pi results for training the Decision Tree.
Pi = [3.125, 3.1605, 3.14285714286, 3.14084507042, 3.14159292035
]
print("Starting Data Transfer") 

for x in range(50000):

    INTERVAL= 1000
    
    circle_points= 0
    square_points= 0
    
    # Total Random numbers generated= possible x
    # values* possible y values
    for i in range(INTERVAL**2):
    
        # Randomly generated x and y values from a
        # uniform distribution
        # Rannge of x and y values is -1 to 1
        rand_x= random.uniform(-1, 1)
        rand_y= random.uniform(-1, 1)
    
        # Distance between (x, y) from the origin
        origin_dist= rand_x**2 + rand_y**2
    
        # Checking if (x, y) lies inside the circle
        if origin_dist<= 1:
            circle_points+= 1
    
        square_points+= 1
    
        # Estimating value of pi,
        # pi= 4*(no. of points generated inside the 
        # circle)/ (no. of points generated inside the square)
        pi = 4* circle_points/ square_points
    
    ##    print(rand_x, rand_y, circle_points, square_points, "-", pi)
    ##    print("\n")
    

    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=[ENTER YOUR ACCESS DATABASE LOCATION HERE];')
    cursor = conn.cursor()
    cursor.execute("Insert into [ENTER YOUR DATABASE TABLE, HERE] ([ENTER YOUR DATABASE TABLE COLUMN, HERE]) values (?)", (pi))
    conn.commit()

print("Data Storage Complete")
   
    
