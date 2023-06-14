import unittest

from src.convert import RegexpToSmtLibConvertor

class TestRegexConvertor(unittest.TestCase):
    def setUp(self):
        self.convertor = RegexpToSmtLibConvertor()

    def test_basic_str(self):
        regex = '2'
        smtlib = '(str.to_re "2")'
        self.assertEqual(self.convertor.convert(regex), smtlib)

    def test_paren_str(self):
        regex = '(2)'
        smtlib = '(str.to_re "2")'
        self.assertEqual(self.convertor.convert(regex), smtlib)

    def test_basic_char_star(self):
            regex = '2*'
            smtlib = '(re.* (str.to_re "2"))'
            self.assertEqual(self.convertor.convert(regex), smtlib)

    def test_basic_char_plus(self):
            regex = '2+'
            smtlib = '(re.+ (str.to_re "2"))'
            self.assertEqual(self.convertor.convert(regex), smtlib)

    def test_basic_concat(self):
        regex = '231*'
        smtlib = '(re.++ (str.to_re "2") (str.to_re "3") (re.* (str.to_re "1")))'
        self.assertEqual(self.convertor.convert(regex), smtlib)

    def test_basic_union(self):
        regex = '23|1*'
        smtlib = '(re.union (re.++ (str.to_re "2") (str.to_re "3")) (re.* (str.to_re "1")))'
        self.assertEqual(self.convertor.convert(regex), smtlib)

    def test_paren_union(self):
        regex = '2(3|a*)'
        smtlib = '(re.++ (str.to_re "2") (re.union (str.to_re "3") (re.* (str.to_re "a"))))'
        self.assertEqual(self.convertor.convert(regex), smtlib)

    def test_allchar_star(self):
        regex = '.*'
        smtlib = '(re.* re.allchar)'
        self.assertEqual(self.convertor.convert(regex), smtlib)

if __name__ == '__main__':
    unittest.main()