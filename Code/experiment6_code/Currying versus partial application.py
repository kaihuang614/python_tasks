def curry_partial(f,*initial_args):
    if not callable(f): 
        return f
    num_args = f.__code__.co_argcount


    if num_args == 0:
        return f(*initial_args)

    if len(initial_args) >= num_args:
        return f(*initial_args[:num_args])

def inner(*params):    
    all_args = [*initial_args, *params]


    if not initial_args:
        return curry_partial(f, *all_args)
    
    if not callable(initial_args[0]):
        return curry_partial(f, *all_args)


    fn = initial_args[0]
    num_args2 = fn.__code__.co_argcount

    if num_args2 == 0:
        return fn(*all_args)

    if len(all_args) >= num_args2:
        return fn(*all_args[:num_args2])
    else:
        return curry_partial(fn, *all_args)
        
    return inner