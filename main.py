import sympy as sp
from sympy.abc import x as sp_x
from sympy.abc import y as sp_y
from itertools import product

# def linear_function(x):
#     return 2.*x - 2.

# def sin_function(x):
#     pi = np.pi
#     return -3.*pi*np.sin(6.*pi*x)

# def my_range(start, end, increment):
#     current = start
#     while current < end:
#         yield current
#         current += increment

# def find_point():
#     results = []
#     for x in my_range(-4., 6., 0.0001):
#         linear_x = linear_function(x)
#         sin_x = sin_function(x)

#         print(f'X = {x}')
#         print(f'Linear X: {linear_x}')
#         print(f'Sin X: {sin_x}')
#         print('')

#         if linear_x == sin_x or abs(linear_x - sin_x) < 0.01:
#             results.append(x)

#     print(results)
#     print('End of calculation!')

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

def get_critical_points(x_set,y_set):
    return list(product(x_set,y_set))

def fxx(x):
    term = -18*(sp.pi**2)*sp.cos(6*sp.pi*sp_x)-2 # −18π²cos(6πx)−2
    return term.evalf(subs={sp_x: x})

def det_H(x,y):
    return fxx(x)*fxx(y)

def test_critical_points(x_set,y_set):
    tested_points = []
    for point in get_critical_points(x_set,y_set):
        tested_points.append({
            point: det_H(point[0],point[1])
        })
    return tested_points

def find_local_optima(x_set, y_set):
    local_optima = []
    for point in test_critical_points(x_set, y_set):
        (key, value), = point.items()
        if value > 0:
            local_optima.append(key)
    return local_optima

def find_optimum_type(x_set,y_set):
    maxima = []
    minima = []
    for point in find_local_optima(x_set,y_set):
        if fxx(point[0]) > 0:
            minima.append(point)
        elif fxx(point[0] < 0):
            maxima.append(point)
    return {
        'maxima': maxima,
        'minima': minima
    }

def test_objective(point):
    objective_function = sp.cos(3*sp.pi*(sp_x+sp_y))*sp.cos(3*sp.pi*(sp_x-sp_y))-sp_x**2-sp_y**2+2*(sp_x-sp_y)+2 # cos[3π(x+y)]cos[3π(x−y)]−x²−y²+2(x−y)+2
    return objective_function.evalf(subs={sp_x: point[0],sp_y: point[1]})

def find_global_optima(x_set,y_set):
    maximum = {}
    minimum = {}
    optima_list = find_optimum_type(x_set,y_set)
    for point in optima_list['maxima']:
        point_value = test_objective(point)
        if maximum['value'] is None or point_value > maximum['value']:
            maximum['point'] = point
            maximum['value'] = point_value
    for point in optima_list['minima']:
        point_value = test_objective(point)
        if minimum['value'] is None or point_value < minimum['value']:
            minimum['point'] = point
            minimum['value'] = point_value
    return {
        'maximum': maximum,
        'minimum': minimum
    }

    
if __name__ == '__main__':
    global_optima = find_global_optima(x_set,y_set)
    if global_optima['maximum']['point']:
        print(f"The greatest value for the objective function is {global_optima['maximum']['value']}")
        print(f"Achieved at point {global_optima['maximum']['point']}")
    if global_optima['minimum']['point']:
        print(f"The smallest value for the objective function is {global_optima['minimum']['value']}")
        print(f"Achieved at point {global_optima['minimum']['point']}")
