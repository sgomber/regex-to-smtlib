import unittest

from src.reg_parser import parser

class TestRegexConvertor(unittest.TestCase):
    def test_basic_str(self):
        regex = '"2"'
        smtlib = '(str.to_re "2")'
        self.assertEqual(parser.parse(regex), smtlib)

    def test_paren_str(self):
        regex = '("2")'
        smtlib = '(str.to_re "2")'
        self.assertEqual(parser.parse(regex), smtlib)

    def test_basic_str_star(self):
            regex = '"2"*'
            smtlib = '(re.* (str.to_re "2"))'
            self.assertEqual(parser.parse(regex), smtlib)

    def test_basic_str_plus(self):
            regex = '"2"+'
            smtlib = '(re.+ (str.to_re "2"))'
            self.assertEqual(parser.parse(regex), smtlib)

    def test_basic_concat(self):
        regex = '"2" ++ "3"'
        smtlib = '(re.++ (str.to_re "2") (str.to_re "3"))'
        self.assertEqual(parser.parse(regex), smtlib)

    def test_basic_union(self):
        regex = '"2" ++ "3" | "1"*'
        smtlib = '(re.union (re.++ (str.to_re "2") (str.to_re "3")) (re.* (str.to_re "1")))'
        self.assertEqual(parser.parse(regex), smtlib)

    def test_paren_union(self):
        regex = '"2" ++ ("3" | "1"*)'
        smtlib = '(re.++ (str.to_re "2") (re.union (str.to_re "3") (re.* (str.to_re "1"))))'
        self.assertEqual(parser.parse(regex), smtlib)

if __name__ == '__main__':
    unittest.main()