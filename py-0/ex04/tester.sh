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
        echo "  expected: $expected"
        echo "  actual:   $actual"
        ((FAIL++))
    fi
}

# Even numbers
check "0 is even"    "I'm Even." "$(python3 whatis.py 0)"
check "2 is even"    "I'm Even." "$(python3 whatis.py 2)"
check "100 is even"  "I'm Even." "$(python3 whatis.py 100)"
check "-2 is even"   "I'm Even." "$(python3 whatis.py -2)"

# Odd numbers
check "1 is odd"     "I'm Odd."  "$(python3 whatis.py 1)"
check "3 is odd"     "I'm Odd."  "$(python3 whatis.py 3)"
check "99 is odd"    "I'm Odd."  "$(python3 whatis.py 99)"
check "-1 is odd"    "I'm Odd."  "$(python3 whatis.py -1)"

# No args — silent return, no output
check "no args: no output" "" "$(python3 whatis.py)"

# Invalid input — AssertionError printed to stdout
check "two args: AssertionError" \
    "AssertionError: more than one argument is provided" \
    "$(python3 whatis.py 1 2)"

check "float arg: AssertionError" \
    "AssertionError: argument is not an integer" \
    "$(python3 whatis.py 1.5)"

check "string arg: AssertionError" \
    "AssertionError: argument is not an integer" \
    "$(python3 whatis.py hello)"

echo ""
echo "Results: $PASS passed, $FAIL failed"
