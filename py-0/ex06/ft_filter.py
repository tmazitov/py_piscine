

def ft_filter(function_to_apply, iterable):
    """Return an iterator yielding those items of iterable for which function
    (item) is true. If function is None, return the items that are true."""
    if function_to_apply is None:
        return (x for x in iterable if x)
    return (x for x in iterable if function_to_apply(x))
