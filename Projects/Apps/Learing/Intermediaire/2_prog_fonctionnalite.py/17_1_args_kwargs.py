def function(nom_arg, *args):
    print(nom_arg)
    print(args)

function(8,1,2,3,4,5)
print()

def ma_func(x, y = 7, *args, **kwargs):
    print(kwargs)

ma_func(2,3,4,5,6, a=7, b=8)