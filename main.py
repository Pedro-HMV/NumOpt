import sympy as sym
from sympy.abc import x as sym_x
from sympy.abc import y as sym_y
from sympy import oo
from itertools import product

class Problem:
    '''
    This class represents the problem at hand: optimizing the objective function
    f(x,y) = cos[3π(x+y)]cos[3π(x−y)]−x²−y²+2(x−y)+2

    Attributes
    ----------
    objective_function : sympy.Expr()
        a simpy expression which stores the function we want to optimize
    x_set : list[float]
        the list of values for x which compose the critical points
    y_set : list[float]
        the list of values for y which compose the critical points
    critical_points : list[tuple[float, float]]
        list of critical points composed from the values in x_set and y_set
    hessian_list : list[dict[tuple[float, float], float]]
        list of dictionaries with a critical point (x,y) as the key and det H(x,y) as the value
    local_optima : list[tuple[float, float]]
        list of optimal points for the function, i.e., det H(x,y) > 0
    optima_by_type : dict[str, list[tuple[float, float]]]
        dictionary with a list of local maxima (identified by the key 'maxima') and a list of local minima (identified by the key 'minima')
    global_optima : dict[str, dict[(str, tuple[float,float]), (str, float)]]
        dictionary that holds the greatest local maximum point with its value and the smallest minimum point with its value

    Methods
    -------
    get_critical_points(x_set, y_set)
        Combines each value of x with each value of y to produce tuples representing critical points
    fxx(x)
        Calculates the second order derivative of the objective function relative to x
        This is sufficient for all second order derivatives in this problem, since its fxx and fyy are the same, and its fxy and fyx are both equal to zero
    det_H(x, y)
        Calculates the determinant of the Hessian matrix for point (x,y)
    get_hessian_list(points)
        Iterates over the list of critical points, calling det_H(x, y) for each of them and storing both point and determinant in a dictionary,
        then appends the dictionary to a list
    get_local_optima(hessian_list)
        Checks the sign of each value in the hessian_list and stores its point in a new list if the value is positive
    get_optimum_type(local_optima)
        Splits the list of local optimal points into a list of local minima and a list of local maxima
    test_objective(point)
        Calculates the value of the objective function for the given point
    get_global_optima(optima_by_type)
        Iterates over the list of local maxima and stores the one with the greatest value
        then does the same for the local minima, but stores the one with the smallest value instead
    '''

    objective_function = sym.cos(3*sym.pi*(sym_x+sym_y))*sym.cos(3*sym.pi*(sym_x-sym_y))-sym_x**2-sym_y**2+2*(sym_x-sym_y)+2 # cos[3π(x+y)]cos[3π(x−y)]−x²−y²+2(x−y)+2

    x_set = [
    -3.595, -3.57,-3.273,-3.226,-2.9473,-2.8847,-2.6202,-2.5452,-2.2923,-2.2064,
    -1.9639,-1.868,-1.635,-1.53,-1.306,-1.192,-0.977,-0.855,-0.648,-0.517,-0.318,
    0.18,0.11,0.157,0.341,0.494,0.67,0.831,1,1.169,1.33,1.506,1.659,1.843,1.989,2.18,
    2.318,2.517,2.648,2.855,2.977,3.192,3.306,3.53,3.635,3.868,3.964,4.206,4.292,4.545,
    4.62,4.885,4.947,5.226,5.273,5.57,5.595
    ]

    y_set = [
    -5.595,-5.57,-5.273,-5.226,-4.947,-4.885,-4.62,-4.545,-4.292,-4.206,-3.964,
    -3.868,-3.635,-3.53,-3.306,-3.192,-2.977,-2.855,-2.648,-2.517,-2.318,-2.18,
    -1.989,-1.843,-1.659,-1.506,-1.33,-1.169,-1,-0.831,-0.67,-0.494,-0.341,
    -0.157,-0.011,0.18,0.318,0.517,0.648,0.855,0.977,1.192,1.306,1.53,1.635,1.868,1.964,
    2.206,2.292,2.545,2.62,2.885,2.947,3.226,3.273,3.57,3.595
    ] 

    def get_critical_points(self, x_set, y_set):
        '''
        Returns a list of tuples representing critical points of the objective function

        Parameters
        ----------
        x_set : list[float]
            List of values for the variable x which vanish the first order derivative of the objective function
        y_set : list[float]
            List of values for the variable y which vanish the first order derivative of the objective function

        Returns
        -------
        critical_points : list[tuple[float,float]]
            List of critical points represented by tuples of floats
        '''

        critical_points = list(product(x_set, y_set))
        return critical_points

    def fxx(self, x):
        '''
        Calculates the second order derivative of dependent variable x

        Parameters
        ----------
        x (float): 
            The variable on which the derivative depends

        Returns
        -------
        derivative : float
            Value of the derivative
        '''

        expr = -18*(sym.pi**2)*sym.cos(6*sym.pi*sym_x)-2 # −18π²cos(6πx)−2
        derivative = expr.evalf(subs={sym_x: x})
        return derivative

    def det_H(self, x, y):
        '''
        Calculates the determinant of the Hessian matrix for point (x,y)

        Parameters
        ----------
        x (float):
            x-coordinate of the critical point
        y (float):
            y-coordinate of the critical point

        Returns
        -------
        determinant : float
            Value of the determinant
        '''

        determinant = self.fxx(x)*self.fxx(y)
        return determinant

    def get_hessian_list(self, points):
        '''
        Iterates over the list of critical points, calling det_H(x, y) for each of them and storing both point and determinant in a dictionary,
        then appends the dictionary to a list

        Parameters
        ----------
        points (list[tuple[float,float]]):
            List of critical points for which to calculate det H(x,y)

        Returns
        -------
        hessian_list : list[dict[tuple[float,float],float]]
            List of points with their determinants
        '''

        hessian_list = []
        for point in points:
            hessian_list.append({
                point: self.det_H(point[0],point[1])
            })
        return hessian_list

    def get_local_optima(self, hessian_list):
        '''
        Checks the sign of each value in the hessian_list and stores its point in a new list if the value is positive

        Parameters
        ----------
        hessian_list : list[dict[tuple[float,float],float]]
            List of dictionaries of form: {
                                        (x,y): det_H(x,y)
                                    }

        Returns
        -------
        local_optima : list[tuple[float,float]]
            List of points for which det H is positive
        '''

        local_optima = []
        for point in hessian_list:
            (key, value), = point.items()
            if value > 0:
                local_optima.append(key)
        return local_optima

    def get_optimum_type(self, local_optima):
        '''
        Splits the list of local optimal points into a list of local minima and a list of local maxima

        Parameters
        ----------
        local_optima : list[tuple[float,float]]
            List of local optimal points

        Returns
        -------
        optima_by_type : dict[str,list[tuple[float,float]]]
            Dictionary of maxima and minima, identified by keys 'maxima' and 'minima', respectively
        '''

        maxima = []
        minima = []
        for point in local_optima:
            if self.fxx(point[0]) > 0:
                minima.append(point)
            elif self.fxx(point[0]) < 0:
                maxima.append(point)
        optima_by_type =  {
            'maxima': maxima,
            'minima': minima
        }
        return optima_by_type

    def test_objective(self, point):
        '''
        Calculates the value of the objective function for the given point

        Parameters
        ----------
        point : tuple[float,float]
            The point (x,y) for which to calculate the value of f(x,y)

        Returns
        -------
        f_value : float
            The value of f(x,y)
        '''

        f_value = self.objective_function.evalf(subs={sym_x: point[0],sym_y: point[1]})
        return f_value

    def get_global_optima(self, optima_by_type):
        '''
        Iterates over the list of local maxima and stores the one with the greatest value
        then does the same for the local minima, but stores the one with the smallest value instead

        Parameters
        ----------
        optima_by_type : dict[str,list[tuple[float,float]]]
            Dictionary of maxima and minima, identified by keys 'maxima' and 'minima', respectively

        Returns
        -------
        global_optima : dict[str,dict[(str,tuple[float,float]),(str,float)]]
            Dictionary that holds the maximum point with the greatest value,
                                  the minimum point with the smallest value
                                  and their respective values:
                                    {
                                        'maximum': {
                                            'point': (x,y),
                                            'value': self.test_objective((x,y))
                                        }
                                    }
        '''

        maximum = {
            'point': (0, 0),
            'value': -9999999
        }
        minimum = {
            'point': (0, 0),
            'value': 9999999
        }
        for point in optima_by_type['maxima']:
            point_value = self.test_objective(point)
            if point_value > maximum['value']:
                maximum['point'] = point
                maximum['value'] = point_value
        for point in optima_by_type['minima']:
            point_value = self.test_objective(point)
            if point_value < minimum['value']:
                minimum['point'] = point
                minimum['value'] = point_value
        global_optima = {
            'maximum': maximum,
            'minimum': minimum
        }
        return global_optima

    def __init__(self):
        self.critical_points = self.get_critical_points(self.x_set, self.y_set)
        self.hessian_list = self.get_hessian_list(self.critical_points)
        self.local_optima = self.get_local_optima(self.hessian_list)
        self.optima_by_type = self.get_optimum_type(self.local_optima)
        self.global_optima = self.get_global_optima(self.optima_by_type)
        self.limit = self.get_limit()
    

if __name__ == '__main__':
    problem = Problem()
    if problem.global_optima['maximum']['point']:
        print(f"The greatest value for the objective function is {problem.global_optima['maximum']['value']}")
        print(f"Achieved at point {problem.global_optima['maximum']['point']}")
    if problem.global_optima['minimum']['point']:
        print(f"The smallest value for the objective function is {problem.global_optima['minimum']['value']}")
        print(f"Achieved at point {problem.global_optima['minimum']['point']}")
