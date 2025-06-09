import math

def cal_triangle_area(width, height):
  return (width * height) / 2

def cal_circle_area(radius):
  return math.pi * radius ** 2

def cal_rectangular_area(width, height, depth):
  return 2 * (width*height + width*depth + height*depth) 
