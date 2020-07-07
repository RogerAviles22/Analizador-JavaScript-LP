import ply.lex as lex

reserved = {
  'if' : 'IF',
  'else' : 'ELSE',
  'elif' : 'ELIF',
  'switch' : 'SWITCH',
  'case' : 'CASE',
  'break' : 'BREAK',
  'default' : 'DEFAULT',
  'for' : 'FOR',
  'var' : 'VAR'

}

tokens = [
    "NUMBER",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "POTENCIA",
    "PUNTOYCOMA",
    "LPAREN",
    "RPAREN",
    "LCORCH",
    "RCORCH",
    "LLLAVE",
    "RLLAVE",
    "COMA",
    "COMILLA",
    "ID",
    "IGUAL"
] + list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_POTENCIA = r'\*\*'
t_PUNTOYCOMA = r'\;'
t_IGUAL = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCORCH = r'\['
t_RCORCH = r'\]'
t_LLLAVE = r'\{'
t_RLLAVE = r'\}'
t_COMA = r'\,'
t_IF = r'if'
t_ELSE = r'else'
t_ELIF = r'elif'
t_SWITCH = r'switch'
t_CASE = r'case'
t_BREAK = r'break'
t_DEFAULT = r'default'
t_FOR = r'for'
t_VAR = r'var'
t_COMILLA = r'\"'



t_ignore = " \t"




#definimos una funcion que castee un valor a NUMBER
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

#definimos una funcion que castee un valor a STRING
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
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
    #print("LexToken(t.type, t.value, t.lineno, t.lexpos)")
    print(tok)


print("Listo lex de PLY")