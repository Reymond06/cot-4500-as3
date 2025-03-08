# README
This program utilzes two methods for solving ordinary differential equations (ODEs): Euler's Method and the Runge-Kutta Method

# Description
Euler's Method: Approximates the solution by iteratively updating y using the slope at the current point. The step size is determined by the total interval divided by the number of iterations

Runge-Kutta Method: Implements the Runge-Kutta algorithm, which computes intermediate slopes (k1, k2, k3, k4) to provide a more accurate update of y

The program sets initial conditions and uses a specified number of iterations to calculate approximate solutions over an interval with both result methods are printed for the user

# Code Explanation
This program takes a function within the function f(t,y) and returns it to main where the range, iteration, and initial point values are stored. The values are then placed into two functions, euler_method() and rk() where they return the values based on Euler's Method and the Range-Kutta Method with the first output based on Euler's Method and the second based on Range-Kutta Method

# Requirements
Since this program utilizes basic Python libraries that are preinstalled, there is no need to install or use any other libraries such as NumPy

# Running the Code
To run the program, please put in your terminal: python assignment_3.py
To run the test program, please put in your terminal: python test_assignment_3.py
