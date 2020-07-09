import ply.lex as lex

reserved = {
  'if' : 'IF',
  'else' : 'ELSE',
  'elif' : 'ELIF',
  'for' : 'FOR',
  'var' : 'VAR',
  'while' : 'WHILE',
  #'String': 'STRING',
  #'Array': 'ARRAY',
  'set': 'SET',
  #'Object': 'OBJECT',
  'console': 'CONSOLE',
  'prompt' : 'PROMPT',
  'new' : 'NEW',
}

tokens = [
    "NUMBER",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "POTENCIA",
    "PUNTO",
    "PUNTOYCOMA",
    "LPAREN",
    "RPAREN",
    "LCORCH",
    "RCORCH",
    "LLLAVE",
    "RLLAVE",
    "COMA",
    "COMILLA",
    "COMILLITA",
    "ID",
    "IGUAL",
    "DOSPUNTOS",
    "AND",
    "OR",
    "NOT",
    "IGUALA",
    "MAYOR",
    "MENOR",
    "DIFERENTE",
    "MAYORIG",
    "MENORIG",
    "METODO",
    "INCREMENTAL",
    "DECREMENTAL",
    "MASGUAL",
    "MENGUAL",
    #"TEXTO",

] + list(reserved.values())

#Operaciones Matemáticas
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_POTENCIA = r'\*\*'
#Simbolos
t_PUNTO = r'\.'
t_PUNTOYCOMA = r'\;'
t_IGUAL = r'='
t_DOSPUNTOS = r':'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCORCH = r'\['
t_RCORCH = r'\]'
t_LLLAVE = r'\{'
t_RLLAVE = r'\}'
t_COMA = r'\,'
t_COMILLA = r'\"'
t_COMILLITA = r'\''
t_INCREMENTAL = r'\+\+'
t_DECREMENTAL = r'--'
t_MASGUAL = r'\+='
t_MENGUAL = r'-='
#Variables y tipos
t_IF = r'if'
t_ELSE = r'else'
t_ELIF = r'elif'
t_FOR = r'for'
t_VAR = r'var'
t_WHILE = r'while'
#t_STRING = r'String'
#t_ARRAY = r'Array'
t_SET = r'Set'
t_NEW = r'new'
#t_OBJECT = r'Object'
t_CONSOLE = r'console'
t_PROMPT = r'prompt'
#Condicionales
t_AND = r'\&\&'
t_OR = r'\|\|'
t_NOT = r'!'
#Comparadores
t_IGUALA = r'=='
t_MAYOR = r'>'
t_MENOR = r'<'
t_DIFERENTE = r'!='
t_MAYORIG = r'>='
t_MENORIG = r'<='
#Digito
t_NUMBER= r'\d+(\.\d+)?'
#t_TEXTO = r'(\".*\"|\'.*\')'
#Solo ingresa letras, no numeros
t_METODO = r'\.([a-z]|[A-Z])+'
#Ignora los espacios y tab
t_ignore = " \t\n"
#Ignora los comentarios que empiezan con numeral // o /* */
t_ignore_COMMENT = r'(//.*|/\*.*\*/)'



#definimos una funcion que castee un valor a NUMBER
"""def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t"""

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




print("EJEMPLOS DE VICTOR\n")

data4 = "var a +=1"
lexenizador(data4,"\nEjemplo1")

data5 = " //este es un comentario"
lexenizador(data5,"\nEjemeplo2")

data6  " if(v.lenght==2): \n console.log('"'c'"')";
lexenizador(data6,"\nEjemplo3")


print("\nEJEMPLOS DE LIVINGSTON\n")

#print("\nEJEMPLO 1\n")
data7 = "var texto = 'Hola mundo.'"        
#Prueba unitaria
lexenizador(data7, "\nEjemplo 1")

#print("\nEJEMPLO 2\n")
data8 = "if (3>5): console.log('Verdadero') else: console.log('Falso')"     
#Prueba unitaria
lexenizador(data8, "\nEjemplo 2")

#print("\nEJEMPLO 3\n")
data9 = "var paises = ['Ecuador', 'Chile', 'Venezuela', 'España']"       
#Prueba unitaria
lexenizador(data9, "\nEjemplo 3")


print("Listo lex de PLY")

