import math
figure=str(input())

if figure =='square':
    a = float(input())
    area = a*a
elif figure =='rectangle':
    a = float(input())
    b = float(input())
    area =a*b
elif figure == 'circle':
    r = float(input())
    area = math.pi*r*r
elif figure == 'triangle':
    a = float(input())
    ha= float(input())
    area=a*ha/2
print(f'{area:.3f}')

