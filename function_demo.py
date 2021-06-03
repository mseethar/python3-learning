#Keyword args

def kwargsfunc(first, second, **nth):
    print(f'first: {first}, second: {second}')
    for k, v in nth.items():
        print(f'key: {k}, value: {v}')

mymap = { "first": 1, 'second': 2, "third": 3, 'fourth': 4 }

kwargsfunc('eins', 'zwei', nth=mymap)

# TypeError: kwargsfunc() got multiple values for argument 'first'
# kwargsfunc('waahat', 'ithnain', **mymap) Cannot mix positional args and keyword args
# kwargsfunc(second='ithnain', first='waahat', **mymap)  Cannot mix positional args and keyword args
kwargsfunc(**mymap)
kwargsfunc(1, 2)


def kwargsfunc2(one, two, three, four):
    pass

kwargsfunc2(**{'one': 1, 'two': 2, 'three': 3, 'four': 4})
