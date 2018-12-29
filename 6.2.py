def story(**kwds):
    return 'once upon a time,there is a'\
'{job} called {name}.'.format_map(kwds)
def power(x,y,*others):
    if others:
        print('received redundant parameters:',others)
    return pow(x,y)
def interval(start,stop=None,step=1):
    'imitates range() for step>0'
    if stop is None:
        start,stop=0,start
        result=[]
        i=start
        while i < stop:
            result.append(i)
            i+=step
        return result