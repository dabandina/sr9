a = int(input('Длина ребра куба: ')) 
h = int(input('Высота цилиндра: ')) 
r = int(input('Радиус основания цилиндра: ')) 
b = int(input('Объем жидкости: ')) 
pi = 3.14
с = a*a*a 
d = r*r*h*pi
if с >= b: 
 def cube():
  print('Жидкость поместится в кубическую емкость') 
else: 
 def cube():
  print('Жидкость не поместится в кубическую емкость') 
  
cube()

if d >= b: 
 def cylinder():
  print('Жидкость поместится в цилиндрическую емкость') 
else:
 def cylinder():
  print('Жидкость не поместится в цилиндрическую емкость') 

cylinder()

if b <= с + d: 
 def both_capacities():
  print('Жидкость поместится в обе емкости') 
else: 
 def both_capacities():
  print('Жидкость не поместится в обе емкости')
  
both_capacities()