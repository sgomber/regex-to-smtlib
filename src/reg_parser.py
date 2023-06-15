from ply.src.ply import yacc
from src.reg_lexer import tokens
from src.smt_regex_constraint_creators import *

def p_s(p):
    '''
    s : s1 END
    '''
    p[0] = p[1][1]

def p_s1(p):
    '''s1 : s1 UNION s2
          | s2'''
    
    # Note: s1 is a tuple -> (list of regex, combined_regex)
    # Where list of regex is the list of all regular expressions it is combined from
    # and the combined_regex is the combined regular expression.
    if len(p) == 4:
        regex_lis = p[1][0]
        regex_lis.append(p[3][1])
        combined_regex = create_union_regex(regex_lis)
        p[0] = (regex_lis, combined_regex)
    else:
        regex = p[1][1]
        regex_lis = [regex]
        p[0] = (regex_lis, regex)

def p_s2(p):
    '''s2 : s2 s3
          | s3'''
    
    # Note: s2 is a tuple -> (list of regex, combined_regex)
    # Where list of regex is the list of all regular expressions it is combined from
    # and the combined_regex is the combined regular expression.
    if len(p) == 3:
        regex_lis = p[1][0]
        regex_lis.append(p[2])
        combined_regex = create_concat_regex(regex_lis)
        p[0] = (regex_lis, combined_regex)
    else:
        regex = p[1]
        regex_lis = [regex]
        p[0] = (regex_lis, regex)

def p_s3(p):
    '''s3 : s4 KSTAR
          | s4 KPLUS
          | s4'''
    if len(p) == 3:
        if p[2] == '+':
            p[0] = create_kplus_regex(p[1])
        else:
            p[0] = create_kstar_regex(p[1])
    else:
        p[0] = p[1]

def p_s4(p):
    '''s4 : CHAR
          | DOT
          | LPAREN s1 RPAREN
          | LBRAC charClasses RBRAC'''
    if len(p) == 2:
        if p[1] == ".":
            p[0] = create_all_char_regex()
        else:
            p[0] = create_regex_from_char(p[1])
    else:
        p[0] = p[2][1]

def p_charClasses(p):
    '''charClasses : charClass charClasses 
                   | charClass'''
    if len(p) == 3:
        regex_lis = p[2][0]
        regex_lis.append(p[1])
        combined_regex = create_union_regex(regex_lis)
        p[0] = (regex_lis, combined_regex)
    else:
        regex = p[1]
        regex_lis = [regex]
        p[0] = (regex_lis, regex)

def p_charClass(p):
    '''charClass : CHAR HYPHEN CHAR
                 | CHAR '''
    if len(p) == 4:
        p[0] = create_range_char_regex(p[1], p[3])
    else:
        p[0] = create_regex_from_char(p[1])

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

if __name__ == "__main__":
    while True:
        try:
            s = input('parse > ')
        except EOFError:
            break
        if not s: continue
        result = parser.parse(s)
        print(result)
