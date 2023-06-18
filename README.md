# regex-to-smtlib
A tool to translate regular expressions to smt-lib constraints

## Instructions

1. Get the code in your machine, either by downloading the zip or using `git clone`.
   Make sure to run the following command to get the `ply` submodule (which is used by the tool):
   ```
   git submodule update --init
   ```
2. Just download the code and use the tool as follows:

    Command:
    ```
    PYTHONPATH=/Users/sgomber/Desktop/Temp/regex-to-smtlib python3 src/convert.py '2(3|1*)'
    ```

    In action:
    ```
    Desktop/Temp/regex-to-smtlib >> PYTHONPATH=/Users/sgomber/Desktop/Temp/regex-to-smtlib python3 src/convert.py '2(3|1*)'            
    (re.++ (str.to_re "2") (re.union (str.to_re "3") (re.* (str.to_re "1"))))
    ```

    In PYTHONPATH, provide the path to the project (both absolute or relative work). The PYTHONPATH can also be set as a variable in the environment.

3. Checkout the tests in [test-converter.py](./tests/test-converter.py) to see the present state of supported syntax.

    The tests can be run using the following command:
    ```
    PYTHONPATH=/Users/sgomber/Desktop/Temp/regex-to-smtlib python3 tests/test-converter.py
    ```

## To Dos

- [x] Optimize the generated regex for char sequences ( (re.++ (str.to_re "a") (str.to_re "b")) -> (str.to_re "ab"))
- [x] Support for . (allchar)
- [ ] See how space (' ') should be handled within regex (is ignored presently, not ideal)
- [ ] Support for re.all and re.none (Will have to think of regex symbols for these)
- [x] Character Sets
- [ ] Anchoring (^$) (not sure if smtlib supports this)
- [ ] Escaped Characters
- [x] ? syntax
- [ ] {m, n} syntax
