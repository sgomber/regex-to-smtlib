# regex-to-smtlib
A tool to translate regular expressions to smt-lib constraints

## Instructions

1. Just download the code and use the tool as follows:

    Command:
    ```
    PYTHONPATH=/Users/sgomber/Desktop/Temp/regex-to-smtlib python3 src/convert.py '"2" ++ ("3" | "1"*)'
    ```

    In action:
    ```
    Desktop/Temp/regex-to-smtlib >> PYTHONPATH=/Users/sgomber/Desktop/Temp/regex-to-smtlib python3 src/convert.py '"2" ++ ("3" | "1"*)'
    (re.++ (str.to_re "2") (re.union (str.to_re "3") (re.* (str.to_re "1"))))
    ```

    In PYTHONPATH, provide the path to the project (both absolute or relative work). The PYTHONPATH can also be set as a variable in the environment.

2. Checkout the tests in [test-converter.py](./tests/test-converter.py) to see the present state of supported syntax.

    The tests can be run using the following command:
    ```
    PYTHONPATH=/Users/sgomber/Desktop/Temp/regex-to-smtlib python3 tests/test-converter.py
    ```

## To Dos


- [ ] Character Sets
- [ ] Anchoring (^?)
- [ ] Escaped Characters
- [ ] Support for ? and {m,n} type syntax
