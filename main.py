import ply.lex as lex

tokens = [
    "NUMBER",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
]

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

t_ignore = " \t"

#definimos una funcion que castee un valor a NUMBER
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

#No identifica el número de linea que va leyendo
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value) #t.lineno es el número de línea actual

def t_error(t):
    print("Caracter no Definido '%s'" % t.value[0])
    t.lexer.skip(1)  #skip(n) Omite n caracteres del input

#Construir el lexer, el encargado de identificar los tokens que han sido definidos
lexer = lex.lex()

#Prueba unitaria
data = input("Ingrese la expresion aritmetica a analizar: ")
lexer.input(data)

while True:
    tok = lexer.token() #Devuelve los tokens que coincida con la entrada
    if not tok:
        break
    print("LexToken(t.type, t.value, t.lineno, t.lexpos)")
    print(tok)

print("Listo lex de PLY")