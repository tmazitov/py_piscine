

def ft_filter(function_to_apply, iterable):
    """Return an iterator yielding items of iterable for which function_to_apply is true."""
    if function_to_apply is None:
        return (x for x in iterable if x)
    return (x for x in iterable if function_to_apply(x))
