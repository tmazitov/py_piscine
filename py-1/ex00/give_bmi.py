

def is_number(value: any) -> bool:
    """Checks if the value is number"""
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def is_nan(value: any) -> bool:
    """Checks if the value is NaN"""
    if isinstance(value, float):
        return value != value  # NaN is not equal to itself
    return False


def validate_list(values: list[int | float]) -> bool:
    """Validates the list of int|float"""
    if not isinstance(values, list):
        return False
    for value in values:
        if not is_number(value) or is_nan(value):
            return False
    return True


def give_bmi(height: list, weight: list) -> list:
    """Calculate the BMI for each pair of height and weight.

    Args:
        height: A list of heights in centimeters.
        weight: A list of weights in kilograms.
    Returns:
        A list of BMIs corresponding to each pair of height and weight.
    """
    try:
        if len(height) != len(weight):
            raise ValueError("lists must be of the same length.")

        heights_valid = validate_list(height)
        weights_valid = validate_list(weight)
        if not heights_valid or not weights_valid:
            raise ValueError("lists must contain only valid numbers.")

        bmi_list = []
        for h, w in zip(height, weight):
            bmi = w / (h ** 2)
            bmi_list.append(bmi)
        return bmi_list
    except ValueError as e:
        print("ValueError:", e)
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Determine if each BMI exceeds the given limit.

    Args:
        bmi: A list of BMIs.
        limit: The BMI limit to compare against.
    Returns:
        A list of booleans indicating whether each BMI exceeds the limit.
    """
    try:
        if not isinstance(limit, (int, float)) or is_nan(limit):
            raise ValueError("Limit must be a number.")
        if not validate_list(bmi):
            raise ValueError("BMI list must contain only valid numbers.")

        return [b > limit for b in bmi]
    except ValueError as e:
        print("ValueError:", e)
        return []
