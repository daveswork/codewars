def row_sum_odd_numbers(n):
    triangle = []
    line = []
    value = 0
    sum = 0
    for i in range(0, n):
        for j in range(0, i+1):
            line.append(value+1)
            value += 2
        triangle.append(line)
        line = []
    for item in triangle[n-1]:
        sum += item
    return sum

print row_sum_odd_numbers(41)

    
