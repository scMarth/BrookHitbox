from decimal import Decimal

b_right = [14.246, 73.114]
b_down = [42.602, 70.388]
b_left = [69.174, 82.151]
b_up = [76.133, 149.302]
b_start = [148.906, 82.151]
b_c_left = [198.266, 133.887]
b_c_down = [198.266, 165.072]
b_gc_a = [220.953, 149.302]
b_square = [227.968, 54.168]
b_triangle = [254.486, 42.172]
b_r1 = [282.841, 45.147]
b_l1 = [309.064, 61.183]
b_x = [227.968, 81.777]
b_circle = [254.486, 69.782]
b_r2 = [282.841, 72.757]
b_l2 = [309.064, 88.793]

coords_list = [
    b_right,
    b_down,
    b_left,
    b_up,
    b_start,
    b_c_left,
    b_c_down,
    b_gc_a,
    b_square,
    b_triangle,
    b_r1,
    b_l1,
    b_x,
    b_circle,
    b_r2,
    b_l2
]

name_list = [
    'b_right',
    'b_down',
    'b_left',
    'b_up',
    'b_start',
    'b_c_left',
    'b_c_down',
    'b_gc_a',
    'b_square',
    'b_triangle',
    'b_r1',
    'b_l1',
    'b_x',
    'b_circle',
    'b_r2',
    'b_l2'
]

reference = b_l1
ref_x, ref_y = reference

reference_position = [0,0]

deltas = []

for coords in coords_list:
    x, y = coords

    deltas.append([Decimal(str(ref_x)) - Decimal(str(x)), Decimal(str(ref_y)) - Decimal(str(y))])

for i in range(0,len(deltas)):
    x_delta, y_delta = deltas[i]

    name = name_list[i].upper()

    print('{} : dx={}, dy={}'.format(name, x_delta, y_delta))



print('sanity check')
print(b_l1[0] - b_right[0])

print(309.064 - 14.246)