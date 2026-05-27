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

# --- From the subject ---
check "'Hello the World' 4 -> ['Hello', 'World']" \
    "['Hello', 'World']" \
    "$(python3 filterstring.py 'Hello the World' 4)"

check "'Hello the World' 99 -> []" \
    "[]" \
    "$(python3 filterstring.py 'Hello the World' 99)"

check "swapped types -> AssertionError" \
    "AssertionError: the arguments are bad" \
    "$(python3 filterstring.py 3 'Hello the World')"

check "no args -> AssertionError" \
    "AssertionError: the arguments are bad" \
    "$(python3 filterstring.py)"

# --- Edge cases ---
check "N=0: all words pass" \
    "['Hello', 'the', 'World']" \
    "$(python3 filterstring.py 'Hello the World' 0)"

check "N=2: words longer than 2" \
    "['Hello', 'the', 'World']" \
    "$(python3 filterstring.py 'Hello the World' 2)"

check "N=3: words strictly longer than 3 (the=3 excluded)" \
    "['Hello', 'World']" \
    "$(python3 filterstring.py 'Hello the World' 3)"

check "single word longer than N" \
    "['Hello']" \
    "$(python3 filterstring.py 'Hello' 3)"

check "single word shorter than N -> []" \
    "[]" \
    "$(python3 filterstring.py 'Hi' 3)"

check "one arg -> AssertionError" \
    "AssertionError: the arguments are bad" \
    "$(python3 filterstring.py 'Hello')"

check "three args -> AssertionError" \
    "AssertionError: the arguments are bad" \
    "$(python3 filterstring.py 'Hello' 4 'extra')"

check "float as N -> AssertionError" \
    "AssertionError: the arguments are bad" \
    "$(python3 filterstring.py 'Hello the World' 4.5)"

check "string as N -> AssertionError" \
    "AssertionError: the arguments are bad" \
    "$(python3 filterstring.py 'Hello the World' abc)"

echo ""
echo "Results: $PASS passed, $FAIL failed"
