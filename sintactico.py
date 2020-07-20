import ply.yacc as sintaxis
import lexico as lex

#import Interfaz as inter
tokens = lex.tokens
#parser = sintaxis.yacc()  
bandera = True

message = ""
#message2 = ""

#Ojo a 'expresion'
def p_sentencias(p):
    '''sentencias : variable sentencias
    | metodos sentencias
    | iteracion sentencias
    | objeto PUNTOYCOMA sentencias
    | newset sentencias
    | array sentencias
    | empty
    | if sentencias
    | while sentencias
    | prompt sentencias
    '''

def p_metodos(p):
    '''metodos : imprimir PUNTOYCOMA
    | metodo PUNTOYCOMA'''

#var _var; var a58a= ''; var _As=54;
def p_variable(p):
   '''variable : VAR ID PUNTOYCOMA 
  | VAR ID IGUAL expresion PUNTOYCOMA 
  | VAR ID IGUAL condi_anidado PUNTOYCOMA 
  '''

#for(i=0; i<=8; i--){sentencias}  
#for(i=0; i<=8; i+=5){sentencias}  
def p_for(p):
  '''iteracion : FOR LPAREN ID IGUAL NUMBER PUNTOYCOMA condicion PUNTOYCOMA ID INDECREMENTAL RPAREN LLLAVE sentencias RLLAVE
  | FOR LPAREN VAR ID IGUAL NUMBER PUNTOYCOMA condicion PUNTOYCOMA ID INDECREMENTAL RPAREN LLLAVE sentencias RLLAVE
  | FOR LPAREN ID IGUAL NUMBER PUNTOYCOMA condicion PUNTOYCOMA ID OPERADORES NUMBER RPAREN LLLAVE sentencias RLLAVE
  | FOR LPAREN VAR ID IGUAL NUMBER PUNTOYCOMA condicion PUNTOYCOMA ID OPERADORES NUMBER RPAREN LLLAVE sentencias RLLAVE'''
  

def p_if(p):
  '''if : IF LPAREN condi_anidado RPAREN LLLAVE sentencias RLLAVE
  | IF LPAREN condi_anidado RPAREN LLLAVE sentencias RLLAVE else
  | IF LPAREN condi_anidado RPAREN LLLAVE sentencias RLLAVE elif
  | IF LPAREN condi_anidado RPAREN LLLAVE sentencias RLLAVE elif else
  '''

def p_else(p):
  'else : ELSE LLLAVE sentencias RLLAVE'

def p_elif(p):
  ''' elif : ELIF LPAREN condi_anidado RPAREN LLLAVE sentencias RLLAVE elif 
  | ELIF LPAREN condi_anidado RPAREN LLLAVE sentencias RLLAVE 
  '''

def p_while(p):
  'while : WHILE LPAREN condi_anidado RPAREN LLLAVE sentencias RLLAVE'

def p_prompt(p):
  '''prompt : VAR ID IGUAL PROMPT LPAREN expresion RPAREN PUNTOYCOMA
  | VAR ID IGUAL PROMPT LPAREN expresion COMA expresion RPAREN PUNTOYCOMA
  '''

#console.log('');
def p_imprimir(p):
  'imprimir : CONSOLE METODO LPAREN expresion RPAREN'

#métodos con y sin argumentos, máximo 2 arg
def p_metodo_argumento0(p):
  'metodo : ID METODO LPAREN RPAREN'

def p_metodo_argumento1(p):
  'metodo : ID METODO LPAREN expresion RPAREN'

def p_metodo_argumento2(p):
  'metodo : ID METODO LPAREN expresion COMA expresion RPAREN'
  
#No es un método, en sí sería el atributo de una variable
def p_metodo_argumento3(p):
  'metodo : ID METODO'

#var id={b:"8", c:(5+2), c:'a'}
def p_objeto(p):
  '''objeto : VAR ID IGUAL LLLAVE RLLAVE  
  | VAR ID IGUAL LLLAVE keyvalue RLLAVE   
  '''
#a:8,   b:"a", c:8.5
def p_objeto_kv(p):
  '''keyvalue : ID DOSPUNTOS factor
  | ID DOSPUNTOS factor COMA keyvalue
  | ID DOSPUNTOS contenido
  | ID DOSPUNTOS contenido COMA keyvalue
  | ID DOSPUNTOS TRUE 
  | ID DOSPUNTOS TRUE COMA keyvalue
  | ID DOSPUNTOS FALSE 
  | ID DOSPUNTOS FALSE COMA keyvalue
  '''

def p_set(p):#confirma Moyarreira
  '''newset : VAR ID IGUAL NEW SET LPAREN RPAREN PUNTOYCOMA
  | VAR ID IGUAL NEW SET LPAREN contenido RPAREN PUNTOYCOMA'''

def p_array(p):
  '''array : VAR ID IGUAL contenido PUNTOYCOMA
  | VAR ID IGUAL NEW ARRAY LPAREN elemento RPAREN PUNTOYCOMA'''

def p_contenido(p):
  '''contenido : LCORCH elemento RCORCH
  | LCORCH RCORCH
  | LCORCH expresion RCORCH'''

def p_elemento(p):
  '''elemento : expresion 
  | expresion COMA elemento '''


#def p_contenido(p):
#  '''contenido : expresion
#      | expresion COMA contenido

#  '''

def p_expresion_suma(p):
    'expresion : expresion PLUS factor'


def p_expresion_resta(p):
    'expresion : expresion MINUS term'

def p_expresion_producto(p):
    'expresion : expresion TIMES term'

def p_expresion_division(p):
    'expresion : expresion DIVIDE term'

def p_expresion_potencia(p):
    'expresion : expresion POTENCIA term'

def p_expression_term(p):
    'expresion : term'

#!(5+8)<2 && a!=3 && 
def p_condicion_operador(p):
  '''condi_anidado : condicion AND condi_anidado
  | NOT condicion AND  condi_anidado 
  | condicion OR  condi_anidado
  | NOT condicion OR  condi_anidado
  | condicion 
  | NOT condicion '''


# (5+2) <,>,<=,>=,!=,== 8
def p_condicion(p):
    '''condicion : factor COMPARADOR factor
    | factor IGUALA factor
    | factor DIFERENTE factor
    | TRUE
    | FALSE
    '''

def p_term_factor(p):
    'term : factor'

def p_factor_expr(p):
    'factor : LPAREN expresion RPAREN'

def p_factor_num(p):
    'factor : NUMBER'

def p_factor_str(p):
    'factor : TEXTO'

def p_factor_var2(p):
    'factor : ID'

#Ayudará para cerrar los bucles de las sentencias?
def p_empty(p):
     'empty :'
     pass

# Error generado
def p_error(p):
  global bandera
  global message
  #global message2
  if p:
    #inter.errorSint.appendPlainText("hola")
    print("Error sintactico del token en la línea: ", p.lineno, " en la posición: ",  p.lexpos, " y token tipo:", p.type)


    line =str(p.lineno)
    lexp =str(p.lexpos)
    type =str(p.type)
    #message = str("Error sintactico del token en la línea: " ,p.lineno, " en la posición: " , p.lexpos , " y token tipo:" , p.type)
    #print(message)
    message += "Error sintactico del token en la línea: "+ line+ " en la posición: "+ lexp+ " y token tipo: "+type+"\n"
    #print(message)


    #message2 = ' '.join(message)
    #print(message2)

    bandera = False
    # Just discard the token and tell the parser it's okay.
    #p.errok()
  else:
        #print("Syntax error at EOF")

        message = "Syntax error at EOF"
        print(message)

        bandera = False

# Construir parser

def sintactico(data):
    global bandera
    global message
    #global mes
    #sintok = []

    parser = sintaxis.yacc()
    result = parser.parse(data)
    if(not bandera):
        sintok = []
        #print("hola" + message)
        sintok.append("Sintaxis Incorrecta")
        sintok.append(message)
        #print("Sintaxis Incorrecta")
        bandera = True
        print(sintok)
        message = ""
        return sintok


        #return message2
    else:
        sintok = []
    #print("Sintaxis Correcta")
        bandera = True
        #return "Sintaxis Correcta"

        sintok.append("Sintaxis Correcta")
        message = ""
        return sintok





    #s= input(data)
'''while True:
  try:
      s = parser.parse(data)

  except EOFError:
    break

  if not s: continue
  result = parser.parse(data)
  #print("Lexpos: ",parser.parse(result,tracking=True))
  if(result == None):
    print("Sintaxis Correcta")   '''

#Roger Avilés
'''
var i; 
var _a2 = []; /*Prueba comentarios*/ 
var A=["a", 5.5]; 
var set= new Set(); 
var set= new Set([]); 
var set= new Set(['a',5]); 
var set1 =5;
for(var i=1; i<=0; i+=2){console.log('a');}
for(var i=1; i<=0; i--){console.log(5+2);}
/*Comentario*/ var i;
// var i;
'''

#Ejemplos de Livingston
'''
#Ejemplos correctos
if (3>5){ console.log('Verdadero');} else{ console.log('Falso');}

var a = prompt("Primer Nivel", "Hola Mundo");

while (true){ console.log('AP en Lenguaje de Programacion'); }

#Ejemplos de errores
var texto = "hola mundo"

if(a>b{var a = 10;}

var er 2 +3

'''

#Ejemplos de Víctor Moyano 
'''if(a>b){var a = 10;}
var conjunto = new Set(["hola","como","estas"]);
console.log("Si se pasa la materia");
var variable = 2;
conjunto.index();
conjunto.metodo("par1",2);'''