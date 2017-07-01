import math

def triangle_type(a, b, c):
    lines=[a,b,c]
    angles = []
    total = 0
    result = 0
    A = 0
    divisor = 0
    dividend = 0
    for i in range(0,3):
        dividend = (float(lines[0]**2 + lines[1]**2 - lines[2]**2))
        divisor =  float(2*lines[0]*lines[1])
        if divisor > 0:
            A = dividend/divisor
            if 1>= A >= -1:
                A = math.acos(A)
                A = math.degrees(A)
                if A > 0:
                    angles.append(A)
                    total += A
        lines[:]=lines[1:] + [lines[0]]
    if 179<= total<=181 and len(angles)==3:
        if 90 in angles:
            result = 2
        elif any(angle>90 for angle in angles):
            result = 3
        elif all(angle<90 for angle in angles):
            result = 1
    else:
        result = 0
    return result

print triangle_type(2,4,6)
