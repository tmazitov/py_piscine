

def is_number(value: any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def slice_me(family: list, start: int, end: int) -> list:
    """Return a slice of the family list from start to end (exclusive).

    Args:
        family: A list of family member names.
        start: The starting index of the slice.
        end: The ending index of the slice (exclusive).
    Returns:
        A list containing the slice of the family list.
    """
    try:
        if not isinstance(family, list):
            raise TypeError("family must be a list")
        if any(not isinstance(index, int) or isinstance(index, bool)
               for index in [start, end]):
            raise TypeError("start and end must be integers")

        old_height = len(family)
        old_width = len(family[0]) if family else 0

        for member in family:
            if not isinstance(member, list):
                raise TypeError("family must be a 2D list")
            if len(member) != old_width:
                raise ValueError("all rows in family must have same length")
            for value in member:
                if not is_number(value):
                    raise ValueError("family must contain only numbers")

        print(f"My shape is : ({old_height}, {old_width})")
        _slice = family[start:end]
        new_height = len(_slice)
        print(f"My new shape is : ({new_height}, {old_width})")

        return _slice

    except (TypeError, ValueError) as e:
        print(f"{type(e).__name__}: {e}")
        return []
