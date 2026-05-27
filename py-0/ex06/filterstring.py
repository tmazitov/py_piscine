import sys
from ft_filter import ft_filter


def is_number(s: str) -> bool:
    """Return True if string s represents a valid integer."""
    try:
        int(s)
        return True
    except ValueError:
        return False


def is_dirty_char(s: str) -> bool:
    """Return True if character is non-printable or invisible."""
    return not s.isprintable() or s == '\n' or s == '\t'


def is_dirty_string(s: str) -> bool:
    """Return True if any character in s is non-printable or invisible."""
    return any(is_dirty_char(c) for c in s)


def validate_args(argv: list[str]) -> bool:
    """Validate that exactly two arguments
    are provided and are of correct types."""
    if len(argv) != 3:
        raise AssertionError("the arguments are bad")

    if not is_number(argv[2]) or int(argv[2]) < 0:
        raise AssertionError("the arguments are bad")

    if is_dirty_string(argv[1]):
        raise AssertionError("the arguments are bad")

    if len(argv[1]) == 0:
        return False

    return True


def main():
    """Entry point: filter words from string S with length greater than N."""
    try:
        argv = sys.argv
        if not validate_args(argv):
            return

        words = argv[1].split()
        length = int(argv[2])
        print([w for w in ft_filter(lambda x: len(x) > length, words)])

    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
