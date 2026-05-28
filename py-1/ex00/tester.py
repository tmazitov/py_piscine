from give_bmi import give_bmi, apply_limit


def main():
    TEST_CASES = [
        # give_bmi: normal cases
        ("basic BMI calculation",                       [22.857142857142858],   lambda: give_bmi([1.75], [70.0])),
        ("multiple values",                             2,                      lambda: len(give_bmi([1.75, 1.80], [70.0, 80.0]))),

        # give_bmi: mismatched lengths
        ("mismatched list lengths → []",                [],                     lambda: give_bmi([1.75, 1.80], [70.0])),

        # give_bmi: wrong types
        ("height not a list → []",                      [],                     lambda: give_bmi("1.75", [70.0])),
        ("weight not a list → []",                      [],                     lambda: give_bmi([1.75], "70.0")),
        ("height contains string → []",                 [],                     lambda: give_bmi([1.75, "1.80"], [70.0, 80.0])),
        ("height contains None → []",                   [],                     lambda: give_bmi([1.75, None], [70.0, 80.0])),
        ("height contains bool → []",                   [],                     lambda: give_bmi([True, 1.80], [70.0, 80.0])),
        ("height contains NaN → []",                    [],                     lambda: give_bmi([float("nan"), 1.80], [70.0, 80.0])),
        ("weight contains inf → not None",              True,                   lambda: give_bmi([1.75], [float("inf")]) is not None),

        # give_bmi: empty lists
        ("empty lists → []",                            [],                     lambda: give_bmi([], [])),

        # apply_limit: normal cases
        ("all above limit",                             [True, True],           lambda: apply_limit([30.0, 35.0], 25)),
        ("all below limit",                             [False, False],         lambda: apply_limit([18.0, 20.0], 25)),
        ("mixed",                                       [False, True],          lambda: apply_limit([20.0, 30.0], 25)),
        ("equal to limit → False",                      [False],                lambda: apply_limit([25.0], 25)),

        # apply_limit: invalid limit
        ("limit is string → []",                        [],                     lambda: apply_limit([22.0], "25")),
        ("limit is None → []",                          [],                     lambda: apply_limit([22.0], None)),
        ("limit is NaN → []",                           [],                     lambda: apply_limit([22.0], float("nan"))),

        # apply_limit: invalid bmi list
        ("bmi contains string → []",                    [],                     lambda: apply_limit([22.0, "bad"], 25)),
        ("bmi contains None → []",                      [],                     lambda: apply_limit([22.0, None], 25)),
        ("bmi not a list → []",                         [],                     lambda: apply_limit("22.0", 25)),

        # apply_limit: empty list
        ("empty bmi list → []",                         [],                     lambda: apply_limit([], 25)),
    ]

    passed = 0
    failed = 0

    for desc, expected, fn in TEST_CASES:
        actual = fn()
        if actual == expected:
            print(f"PASS: {desc}")
            passed += 1
        else:
            print(f"FAIL: {desc}")
            print(f"  expected: {expected}")
            print(f"  actual:   {actual}")
            failed += 1

    print(f"\nResults: {passed} passed, {failed} failed")


if __name__ == '__main__':
    main()
