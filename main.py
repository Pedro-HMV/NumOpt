import sympy as sym
from sympy.abc import x as sym_x
from sympy.abc import y as sym_y
from sympy import oo
from itertools import product
from sympy.plotting import plot, plot3d

class Problem:
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

    critical_points = []
    hessian_list = []
    local_optima = []
    optima_by_type = {}
    global_optima = {}

    def get_critical_points(self, x_set, y_set):
        return list(product(x_set, y_set))

    def fxx(self, x):
        expr = -18*(sym.pi**2)*sym.cos(6*sym.pi*sym_x)-2 # −18π²cos(6πx)−2
        return expr.evalf(subs={sym_x: x})

    def det_H(self, x, y):
        return self.fxx(x)*self.fxx(y)

    def get_hessian_list(self, points):
        hessian_list = []
        for point in points:
            hessian_list.append({
                point: self.det_H(point[0],point[1])
            })
        return hessian_list

    def get_local_optima(self, hessian_list):
        local_optima = []
        for point in hessian_list:
            (key, value), = point.items()
            if value > 0:
                local_optima.append(key)
        return local_optima

    def get_optimum_type(self, local_optima):
        maxima = []
        minima = []
        for point in local_optima:
            if self.fxx(point[0]) > 0:
                minima.append(point)
            elif self.fxx(point[0]) < 0:
                maxima.append(point)
        return {
            'maxima': maxima,
            'minima': minima
        }

    def test_objective(self, point):
        return self.objective_function.evalf(subs={sym_x: point[0],sym_y: point[1]})

    def get_global_optima(self, optima_by_type):
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
        return {
            'maximum': maximum,
            'minimum': minimum
        }

    def get_limit(self):
        f = -(sym_x**2)-(sym_y**2)+2*sym_x-2*sym_y+2
        return sym.limit(sym.limit(f, sym_x, oo), sym_y, oo)


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
    print(problem.limit)
    # plot3d(problem.objective_function)
