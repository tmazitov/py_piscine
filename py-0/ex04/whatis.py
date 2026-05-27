import sys


def odd_check(num: int) -> bool:
    return num & 1


def is_number(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False


def validate_args(argv: list[str]) -> bool:

    if len(argv) == 1:
        return False

    if len(argv) != 2:
        raise AssertionError("more than one argument is provided")
    if not is_number(argv[1]):
        raise AssertionError("argument is not an integer")

    return True


def main():
    try:
        argv = sys.argv
        if not validate_args(argv):
            return

        is_odd = odd_check(int(argv[1]))
        if is_odd:
            print("I'm Odd.")
        else:
            print("I'm Even.")
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
