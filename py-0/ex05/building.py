import sys


def validate_args(argv: list[str]) -> bool:
    """Validate that at most one argument is provided."""
    if len(argv) > 2:
        raise AssertionError("more than one argument is provided")

    return True


def count_letters(text: str) -> dict[str, int]:
    """Count uppercase, lowercase, punctuation, space and digit characters."""
    letter_count = {
        "up": 0,
        "low": 0,
        "punct": 0,
        "space": 0,
        "digit": 0,
    }
    for char in text:
        if char.isupper():
            letter_count["up"] += 1
        elif char.islower():
            letter_count["low"] += 1
        elif char.isspace():
            letter_count["space"] += 1
        elif char.isdigit():
            letter_count["digit"] += 1
        else:
            letter_count["punct"] += 1
    return letter_count


def main():
    """Entry point: count character types in the given string argument."""
    try:
        argv = sys.argv
        if not validate_args(argv):
            return

        if len(argv) == 1 or len(argv[1]) == 0:
            print("What is the text to count?")
            text = sys.stdin.readline()
            text = text.rstrip("\n")
        else:
            text = argv[1]

        stats = count_letters(text)
        print(f"""The text contains {len(text)} characters:
{stats['up']} upper letters
{stats['low']} lower letters
{stats['punct']} punctuation marks
{stats['space']} spaces
{stats['digit']} digits""")

    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
