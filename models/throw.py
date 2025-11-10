
value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25]
multiplier = [1, 2, 3]

def points(dart, dart_pos):
    round_point = value[dart] * multiplier[dart_pos]
    return round_point