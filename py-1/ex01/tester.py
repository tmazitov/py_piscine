from array2D import slice_me


def main():
    valid = [[1.80, 78.4], [2.15, 102.7], [1.88, 75.2]]

    test_cases = [
        # normal slices
        ("basic slice [0:2]",
         [[1.80, 78.4], [2.15, 102.7]],
         lambda: slice_me(valid, 0, 2)),

        ("negative end [1:-1]",
         [[2.15, 102.7]],
         lambda: slice_me(valid, 1, -1)),

        ("full slice [0:3]",
         valid,
         lambda: slice_me(valid, 0, 3)),

        ("start == end -> []",
         [],
         lambda: slice_me(valid, 1, 1)),

        ("start > end -> []",
         [],
         lambda: slice_me(valid, 2, 1)),

        ("out of bounds end -> truncated",
         valid,
         lambda: slice_me(valid, 0, 100)),

        ("single row family",
         [[1.80, 78.4]],
         lambda: slice_me([[1.80, 78.4]], 0, 1)),

        ("empty family -> []",
         [],
         lambda: slice_me([], 0, 1)),

        # family type errors
        ("family not a list -> []",
         [],
         lambda: slice_me("not a list", 0, 2)),

        ("family is tuple -> []",
         [],
         lambda: slice_me(((1.80, 78.4), (2.15, 102.7)), 0, 1)),

        ("row not a list -> []",
         [],
         lambda: slice_me([(1.80, 78.4), [2.15, 102.7]], 0, 1)),

        # uneven rows
        ("uneven row lengths -> []",
         [],
         lambda: slice_me([[1.80, 78.4], [2.15]], 0, 2)),

        # invalid values in rows
        ("row contains string -> []",
         [],
         lambda: slice_me([[1.80, "bad"], [2.15, 102.7]], 0, 2)),

        ("row contains None -> []",
         [],
         lambda: slice_me([[1.80, None], [2.15, 102.7]], 0, 2)),

        ("row contains bool -> []",
         [],
         lambda: slice_me([[True, 78.4], [2.15, 102.7]], 0, 2)),

        # start/end type errors
        ("start is float -> []",
         [],
         lambda: slice_me(valid, 0.0, 2)),

        ("end is float -> []",
         [],
         lambda: slice_me(valid, 0, 2.0)),

        ("start is string -> []",
         [],
         lambda: slice_me(valid, "0", 2)),

        ("start is None -> []",
         [],
         lambda: slice_me(valid, None, 2)),

        ("start is bool -> []",
         [],
         lambda: slice_me(valid, True, 2)),
    ]

    passed = 0
    failed = 0

    for desc, expected, fn in test_cases:
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
