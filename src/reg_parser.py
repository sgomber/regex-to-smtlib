from ply.src.ply import yacc
from src.reg_lexer import tokens
from src.smt_regex_constraint_creators import *

def p_s(p):
    '''
    s : s1 END
    '''
    p[0] = p[1]

def p_s1(p):
    '''s1 : s1 UNION s2
          | s2'''
    if len(p) == 4:
        p[0] = create_union_regex(p[1], p[3])
    else:
        p[0] = p[1]

def p_s2(p):
    '''s2 : s2 s3
          | s3'''
    if len(p) == 3:
        p[0] = create_concat_regex(p[1], p[2])
    else:
        p[0] = p[1]

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
          | LPAREN s1 RPAREN'''
    if len(p) == 2:
        p[0] = create_regex_from_char(p[1])
    else:
        p[0] = p[2]

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
