#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 23:18:15 2018

@author: KimSooHyeon
"""
import numpy as np

class Vector(object):
    
    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __repr__(self):
        return 'Vector: {}'.format(self.coordinates)
    
    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)
    def __eq__(self, v):
        return self.coordinates == v.coordinates
    
    def plus(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, c):
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(new_coordinates)
    
    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return np.sqrt(np.sum(coordinates_squared))
    
    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1./magnitude)
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)
    
    def is_orthogonal_to(self, v,tolerence = 1e-10):
        return abs(self.dot(v)) < tolerence
    
    def is_parallel_to(self, v):
        return (self.is_zero() or v.is_zero() or \
                self.angle_with(v) == 0 or \
                self.angle_with(v) == np.pi   )         
    
    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance
    
    def dot(self, v):
        coordinates_products = [x*y for x, y in zip(self.coordinates, v.coordinates)]
        return np.sum(coordinates_products)
        
    def angle_with(self, v, in_degrees=False):
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            angle_in_radians = np.arccos(np.clip(u1.dot(u2), -1, 1))
            
            if in_degrees:
                return np.degrees(angle_in_radians)
            else:
                return angle_in_radians
            
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an an angle with the zero vector')
            else:
                raise e

## [Test]: try these on console
#v = Vector([1,-1,2])
#w= Vector([-1, 1, 1])
#v
#w
#v.plus(w)
#v.minus(w)        
#v.times_scalar(2)
#v.magnitude()
#v.normalized()
#v.is_orthogonal_to(w)
#v.is_parallel_to(w)
#v.is_zero()
#v.dot(w)
#v.angle_with(w)
#v.angle_with(w, True)

