class Poly(object):
    def __init__(self, *constants):
        self.constants = list(constants)
        self.deg = len(self.constants) - 1

    def __repr__(self):
        return "Polynomial" + str(self.constants)

    def eval(self, x):
        val = 0
        for power, coef in enumerate(self.constants):
            val += coef * (x ** power)
        return val

    def deriv(self):
        der_constants1 = []
        for power, coef in enumerate(self.constants):
            der_constants1.append(coef * power)
        #print(der_constants)
        der_constants1.remove(der_constants1[0])
        return der_constants1

    def deriv_eval(self, x):
        self.der_constants = []
        val = 0
        #generate the list representing constants of derivative
        for power, coef in enumerate(self.constants):
            self.der_constants.append(coef * power)
        self.der_constants.remove(self.der_constants[0])
        for power, coef in enumerate(self.der_constants):
            val += coef * (x ** power)
        #return value of derivative
        return val

def deriv(poly_list):
    der_constants1 = []
    for power, coef in enumerate(poly_list):
        der_constants1.append(coef * power)
    #print(der_constants)
    der_constants1.remove(der_constants1[0])
    return der_constants1

def f(p, x):
    if isinstance(p, list):
        val = 0
        for power, coef in enumerate(p):
            val += coef * (x ** power)
        #return value of derivative
        return val
    else:
        return p.eval(x)


def bisec(p, a, b, precision):
    check = False
    if f(p, a) == f(p, b):
        print("This is an invalid function.")
        return

    while(b-a >= 10**(-precision)):
        check = True
        #finding middle point
        c = (a + b) / 2
        #check if middle point is root
        if f(p, c) == 0.0:
            break
        #finding the side to repeat
        if f(p, c) * f(p, a) < 0:
            b = c
        else:
            a = c
    if check == True:
        bound = "%."+str(precision)+"f"
        print("The root value is: ", bound % c)
        return c

def kth_deriv(poly_list, steps_up_from_linear):
    if len(poly_list) <= 2 + steps_up_from_linear:
        #print(poly_list)
        return (poly_list)
    else:
        der = deriv(poly_list)
        return (kth_deriv(der, steps_up_from_linear))

def solve_P(poly_list):
    L = poly_list
    return (-L[0]/L[1])

def check_bisections(pivot_list, poly_list):
    #print(poly_list)
    #print(pivot_list)
    #here poly function is the function we are checking for roots
    roots_new = []
    mid = []
    #print(bisec(poly_list, -10**6, pivot_list[0], 5))
    #print(roots)
    if len(pivot_list) >= 2:
        for i in range(0, len(pivot_list) - 1): #this is meant to go up to but not include i+1 = the last element, so this may need to be adjusted
            start = [bisec(poly_list, -10**6, pivot_list[0], 5)]
            m = [bisec(poly_list, pivot_list[i], pivot_list[i+1], 5)]
            mid = mid + m
            end = [bisec(poly_list, pivot_list[len(pivot_list) - 1], 10**6, 5)]
            roots_new = start + mid + end
    else:
        start = (bisec(poly_list, -10**6, pivot_list[0], 5))
        roots_new.append(start)
        end = bisec(poly_list, pivot_list[len(pivot_list)-1], 10**6, 5)
        end = [end]
        #print(end)
        roots_new = roots_new + end
    print("And the root values are for the polynomial degree", len(pivot_list) + 1)
    print(roots_new)

    #roots.append(end)
    #print(roots)

    #print(roots)
    return roots_new

def roots(poly_list):#takes in linear function first
    pivot_list = []
    iterations = len(poly_list) - 1
    pivot_list.append(solve_P(kth_deriv(poly_list, 0)))
    for i in range(1, iterations):#may need to be adjusted by one
        pivot_list = check_bisections(pivot_list, kth_deriv(poly_list, i))
    return pivot_list

if __name__ == "__main__":
    p = Poly(-1, 3, 4, 1)
    x_0 = 0
    x = 2

    print("The following is the polynomial represented: ")
    print(p.__repr__())
    print("")

    print("The following is the polynomial derivative represented: ")
    print(p.deriv())
    print("")

    print("The following num is the degree of the poly:")
    print(p.deg)
    print("")

    print("The following are the x and y values of the polynomial respectively from x =", x_0, " to ", x)
    for x in range(x_0,x+1):
        print(x, p.eval(x))
    print("")

    print("Bisection of the polynomial: ")
    bisec(p, 0, 4, 5)
    print("")

    print("Critical value of polynomial derivative: ")
    roots(p.constants)
