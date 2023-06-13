from ply.src.ply import lex

tokens = (
   'CONCAT',
   'UNION',
   'STR',
   'KPLUS',
   'KSTAR',
   'LPAREN',
   'RPAREN'
)

t_UNION  = r'\|'
t_CONCAT   = r'\+\+'
t_STR     = r'"[^\"]*"'
t_KSTAR   = r'\*'
t_KPLUS   = r'\+'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

if __name__ == "__main__":
    # # Test it out
    data = '"s" ++ "r"'

    # # Give the lexer some input
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok.type, tok.value, tok.lineno, tok.lexpos)