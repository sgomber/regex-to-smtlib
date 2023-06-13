# regex-to-smtlib
A tool to translate regular expressions to smt-lib constraints

## Instructions

1. Just download the code and use the tool as follows:

    ```
    Desktop/Temp/regex-to-smtlib >> PYTHONPATH=/Users/sgomber/Desktop/Temp/regex-to-smtlib python3 src/convert.py '"2" ++ ("3" | "1"*)'
    (re.++ (str.to_re "2") (re.union (str.to_re "3") (re.* (str.to_re "1"))))
    ```

    In PYTHONPATH, provide the path to the project (both absolute or relative work). The PYTHONPATH can also be set as a variable in the environment.


## To Dos


- [ ] Character Sets
- [ ] Anchoring (^?)
- [ ] Escaped Characters
- [ ] Support for ? and {m,n} type syntax
