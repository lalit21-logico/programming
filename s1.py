
def function_name(coordinates):
    n = len(coordinates)
    slope_map = {}
    result = 0
    #count  = 0
    # for x in coordinates:
    for i in range(n):
        slope_map.clear()
        same, vertical = 1, 0
        slope_max = 0
        for j in range(i + 1, n):
            dx, dy = coordinates[i][0] - \
                coordinates[j][0], coordinates[i][1] - coordinates[j][1]
            if dx == dy == 0:
                same += 1
            elif dx == 0:
                vertical += 1
            else:
                slope = float(dy) / float(dx)
                slope_map[slope] = slope_map.get(slope, 0) + 1
                slope_max = max(slope_max, slope_map[slope])
        result = max(result, max(slope_max, vertical) + same)
        # print(slope_map)

    return result


A = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
print(Sr(A))
