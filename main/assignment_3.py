def f(t, y):
    return # Insert function

# Euler Method Function
def euler_method(f, x0, y0, t_end, iter):
    h = (t_end - x0) / iter  
    t = x0
    y = y0
    for _ in range(iter):
        y = y + h * f(t, y)
        t = t + h
    return y

# Runge-Kutta Method Function
def rk(f, x0, y0, t_end, iter):
    h = (t_end - x0) / iter  
    t = x0
    y = y0
    for _ in range(iter):
        k1 = f(t, y)
        k2 = f(t + h/2, y + h/2 * k1)
        k3 = f(t + h/2, y + h/2 * k2)
        k4 = f(t + h, y + h * k3)
        y = y + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
        t = t + h
    return y

def main():
    
    x = # Insert x-value
    y = # Insert y-value
    end = # Insert end value of interval
    iterations = # Insert number of iterations

    # Calls both functions
    euler_result = euler_method(f, x, y, end, iterations)
    rk_result = rk(f, x, y, end, iterations)

    # Prints results of the functions
    print( euler_result)
    print(rk_result)
main()