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
        smtlib = '(re.++ (str.to_re "23") (re.* (str.to_re "1")))'
        self.assertEqual(self.convertor.convert(regex), smtlib)

    def test_basic_union(self):
        regex = '23|1*'
        smtlib = '(re.union (str.to_re "23") (re.* (str.to_re "1")))'
        self.assertEqual(self.convertor.convert(regex), smtlib)

    def test_adv_union(self):
        regex = '1|2*3|3'
        smtlib = '(re.union (str.to_re "1") (re.++ (re.* (str.to_re "2")) (str.to_re "3")) (str.to_re "3"))'
        self.assertEqual(self.convertor.convert(regex), smtlib)

    def test_paren_union(self):
        regex = '2(3|a*)'
        smtlib = '(re.++ (str.to_re "2") (re.union (str.to_re "3") (re.* (str.to_re "a"))))'
        self.assertEqual(self.convertor.convert(regex), smtlib)

    def test_allchar_star(self):
        regex = '.*'
        smtlib = '(re.* re.allchar)'
        self.assertEqual(self.convertor.convert(regex), smtlib)
    
    def test_char_ranges(self):
        regex = '[a-zY-Z3]+'
        smtlib = '(re.+ (re.union (str.to_re "3") (re.range "Y" "Z") (re.range "a" "z")))'
        self.assertEqual(self.convertor.convert(regex), smtlib)

    def test_char_seq_merge_optimization(self):
        regex = 'ab|a|22*3a'
        smtlib = '(re.union (str.to_re "ab") (str.to_re "a") (re.++ (str.to_re "2") (re.* (str.to_re "2")) (str.to_re "3a")))'
        self.assertEqual(self.convertor.convert(regex), smtlib)

if __name__ == '__main__':
    unittest.main()