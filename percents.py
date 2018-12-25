def percents(x,y):
    one_precents = x / 100
    result = y / one_precents
    return result


def print_percents(x,y):
    '''Print what percentage of x is y'''
    print(str(y) + ' is ' + str(percents(x,y)) + ' rercents of ' + str(x))


print_percents(200, 50)
