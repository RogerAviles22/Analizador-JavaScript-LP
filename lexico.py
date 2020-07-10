import ply.lex as lex

reserved = {
  'if' : 'IF',
  'else' : 'ELSE',
  'elif' : 'ELIF',
  'for' : 'FOR',
  'var' : 'VAR',
  'while' : 'WHILE',
  'set': 'SET',
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
    "DIFERENTE",
    "METODO",
    "INCREMENTAL",
    "DECREMENTAL",
    "OPERADORES",
    "TEXTO",
    "COMPARADOR",

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
t_OPERADORES = r'(\+|-|\*|/|\*\*)='
#Variables y tipos
t_IF = r'if'
t_ELSE = r'else'
t_ELIF = r'elif'
t_FOR = r'for'
t_VAR = r'var'
t_WHILE = r'while'
t_SET = r'Set'
t_NEW = r'new'
t_CONSOLE = r'console'
t_PROMPT = r'prompt'
#Condicionales
t_AND = r'\&\&'
t_OR = r'\|\|'
t_NOT = r'!'
#Comparadores
t_IGUALA = r'=='
t_DIFERENTE = r'!='
t_COMPARADOR = r'[<>]=?' #Compara con < , >, <=, >=
#Digito
t_NUMBER= r'\d+(\.\d+)?'
#CADENA
t_TEXTO = r'(\'[a-zA-Z0-9\!\s\.,:À-ÿ\u00f1\u00d1]*\'|\"[a-zA-Z0-9\!\s\.,:À-ÿ\u00f1\u00d1]*\")'
#t_TEXTO= r'\'.*\'' Lee todo como texto desde donde empieza la comilla hasta donde termine
#Ej: var paises = ['Ecuador', 'Chile', 'Venezuela', 'Argentina'] todo desde 'Ecuador...Argentina' lo considera texto
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

def lexenizador(data, mensaje):
  print("\nCódigo: \n"+data+"\n")
  #Construir el lexer, el encargado de identificar los tokens que han sido definidos
  lexer = lex.lex()
  lexer.input(data)
  print(mensaje)
  while True:
    #Devuelve los tokens que coincida con la entrada
      tok = lexer.token() 
      if not tok:
          break
      #print("LexToken(t.type, t.value, t.lineno, t.lexpos)")
      print(tok)

print("EJEMPLOS DE ROGER\n")
#9 lineas validadas de los integrantes
data1 = """for( var i=0 ; i<8 ; i++ ){
    /*Comentario mi llave*/ 
    //Comentario de largoooooo
    var _texto = 'Prueba 1.1 8556 8,6 con ñÑ y tíldéÁ';
    var Texto8= "Prueba 2 con ñ y tíldé Con símbolos permitidos !.:,";
} \n"""        

data2 = """while( (5>=8 && !(9<2)) || x<y || a!=b){
  var objecto1 = {
    a: 'somestring',
    b: 42,
    c: 45.89524
   }
   a+=5;
   x**=8;
   b++;
}"""
data3 = """var nombre =prompt('Ingrese su nombre:');
nombre.length"""

lexenizador(data1, "Ejercicio 1")
lexenizador(data2, "Ejercicio 2")
lexenizador(data3, "Ejercicio 3")

print("\nEJEMPLOS DE VICTOR\n")

data4 = "var a = new Set();"
lexenizador(data4,"\nEjemplo1")

data5 = " //este es un comentario \n var suma= 5+8"
lexenizador(data5,"\nEjemplo2")

data6 = " if(v.lenght==2): \n console.log('"'c'"');";
lexenizador(data6,"\nEjemplo3")


print("\nEJEMPLOS DE LIVINGSTON\n")

#print("\nEJEMPLO 1\n")
data7 = "var texto = 'Hola mundo.'"        
#Prueba unitaria
lexenizador(data7, "\nEjemplo 1")

#print("\nEJEMPLO 2\n")
data8 = "if (3>5): console.log('Verdadero'); else: console.log('Falso');"     
#Prueba unitaria
lexenizador(data8, "\nEjemplo 2")

#print("\nEJEMPLO 3\n")
data9 = "var paises = ['Ecuador', 'Chile', 'Venezuela', 'Argentina'] \nvar aumentar=5; aumentar*=8; aumentar/=10.5; aumentar++; aumentar--; aumentar=20;"       
#Prueba unitaria
lexenizador(data9, "\nEjemplo 3")

print("Listo lex de PLY")