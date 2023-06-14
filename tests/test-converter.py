import unittest

from src.convert import RegexpToSmtLibConvertor

class TestRegexConvertor(unittest.TestCase):
    def setUp(self):
        self.convertor = RegexpToSmtLibConvertor()

    def test_basic_str(self):
        regex = '"2"'
        smtlib = '(str.to_re "2")'
        self.assertEqual(self.convertor.convert(regex), smtlib)

    def test_paren_str(self):
        regex = '("2")'
        smtlib = '(str.to_re "2")'
        self.assertEqual(self.convertor.convert(regex), smtlib)

    def test_basic_str_star(self):
            regex = '"2"*'
            smtlib = '(re.* (str.to_re "2"))'
            self.assertEqual(self.convertor.convert(regex), smtlib)

    def test_basic_str_plus(self):
            regex = '"2"+'
            smtlib = '(re.+ (str.to_re "2"))'
            self.assertEqual(self.convertor.convert(regex), smtlib)

    def test_basic_concat(self):
        regex = '"2""3"'
        smtlib = '(re.++ (str.to_re "2") (str.to_re "3"))'
        self.assertEqual(self.convertor.convert(regex), smtlib)

    def test_basic_union(self):
        regex = '"2""3" | "1"*'
        smtlib = '(re.union (re.++ (str.to_re "2") (str.to_re "3")) (re.* (str.to_re "1")))'
        self.assertEqual(self.convertor.convert(regex), smtlib)

    def test_paren_union(self):
        regex = '"2"("3" | "1"*)'
        smtlib = '(re.++ (str.to_re "2") (re.union (str.to_re "3") (re.* (str.to_re "1"))))'
        self.assertEqual(self.convertor.convert(regex), smtlib)

if __name__ == '__main__':
    unittest.main()