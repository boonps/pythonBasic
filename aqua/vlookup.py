aqi_tbl = [[0, 'great', "blue"],
           [26, 'good', "red"],
           [51, 'moderate', "green"],
           [101, 'unhealthy', "black"],
           [201, 'very unhealthy', "white"],
           ]

grade_tbl = [
    [0, "F"],
    [50, "D"],
    [70, "C"],
    [80, "B"],
    [90, "A"]
]


def vlookup(v, tbl, col):
    # x = filter(lambda n: v >= n[0], tbl)
    # # print(list(x))
    # print(max(x)[col])
    # return 0
    # r = (lambda n: v >= n[0], tbl))
    # return r[col]
    return max(filter(lambda n: v >= n[0], tbl))[col]


if __name__ == '__main__':
    aqi = 20
    # score = 99
    print(vlookup(aqi, aqi_tbl, 2))
    # print(vlookup(score, grade_tbl, 1))
