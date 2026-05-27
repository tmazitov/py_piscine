#!/bin/bash

PASS=0
FAIL=0

check() {
    local desc="$1"
    local expected="$2"
    local actual="$3"

    if [ "$actual" = "$expected" ]; then
        echo "PASS: $desc"
        ((PASS++))
    else
        echo "FAIL: $desc"
        echo "  expected: |$expected|"
        echo "  actual:   |$actual|"
        ((FAIL++))
    fi
}

# Mixed content
check "Hello, World!" \
"The text contains 13 characters:
2 upper letters
8 lower letters
2 punctuation marks
1 spaces
0 digits" \
"$(python3 building.py "Hello, World!")"

# Only lowercase
check "only lowercase" \
"The text contains 5 characters:
0 upper letters
5 lower letters
0 punctuation marks
0 spaces
0 digits" \
"$(python3 building.py "hello")"

# Only uppercase
check "only uppercase" \
"The text contains 5 characters:
5 upper letters
0 lower letters
0 punctuation marks
0 spaces
0 digits" \
"$(python3 building.py "HELLO")"

# Only digits
check "only digits" \
"The text contains 4 characters:
0 upper letters
0 lower letters
0 punctuation marks
0 spaces
4 digits" \
"$(python3 building.py "1234")"

# Only spaces
check "only spaces" \
"The text contains 3 characters:
0 upper letters
0 lower letters
0 punctuation marks
3 spaces
0 digits" \
"$(python3 building.py "   ")"

# Only punctuation
check "only punctuation" \
"The text contains 3 characters:
0 upper letters
0 lower letters
3 punctuation marks
0 spaces
0 digits" \
"$(python3 building.py "!@#")"

# Mixed digits and letters
check "Hello World 123" \
"The text contains 15 characters:
2 upper letters
8 lower letters
0 punctuation marks
2 spaces
3 digits" \
"$(python3 building.py "Hello World 123")"

# Empty string arg — reads from stdin (newline stripped)
check "empty arg reads from stdin" \
"What is the text to count?
The text contains 5 characters:
1 upper letters
4 lower letters
0 punctuation marks
0 spaces
0 digits" \
"$(echo "Hello" | python3 building.py "")"

# No args — reads from stdin (newline stripped)
check "no args reads from stdin" \
"What is the text to count?
The text contains 12 characters:
2 upper letters
8 lower letters
1 punctuation marks
1 spaces
0 digits" \
"$(echo "Hello World!" | python3 building.py)"

# Two args — AssertionError
check "two args: AssertionError" \
"AssertionError: more than one argument is provided" \
"$(python3 building.py arg1 arg2)"

echo ""
echo "Results: $PASS passed, $FAIL failed"
