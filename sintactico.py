import ply.yacc as sintaxis
import lexico as lex
tokens = lex.tokens

#Ojo a 'expresion'
def p_sentencias(p):
    '''sentencias : variable sentencias
    | expresion sentencias
    | metodos sentencias
    | iteracion sentencias
    | objeto PUNTOYCOMA sentencias
    | newset sentencias
    | array sentencias
    | empty
    '''

def p_metodos(p):
    '''metodos : imprimir PUNTOYCOMA
    | condi_anidado
    | metodo PUNTOYCOMA'''

#var _var; var a58a= ''; var _As=54;
def p_variable(p):
   '''variable : VAR ID PUNTOYCOMA
  | VAR ID IGUAL expresion PUNTOYCOMA
  | VAR ID IGUAL condi_anidado PUNTOYCOMA
  '''

#for(i=0; i<=8; i--){}  
def p_for(p):
  '''iteracion : FOR LPAREN ID IGUAL NUMBER PUNTOYCOMA condicion PUNTOYCOMA ID INDECREMENTAL RPAREN LLLAVE sentencias RLLAVE'''
  
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
  '''keyvalue : ID DOSPUNTOS factor COMA keyvalue
  | ID DOSPUNTOS factor COMA
  '''

def p_set(p):#confirma Movarreira
  '''newset : VAR ID IGUAL NEW SET LPAREN RPAREN PUNTOYCOMA
  | VAR ID IGUAL NEW SET LPAREN contenido RPAREN PUNTOYCOMA'''

def p_array(p):
  'array : VAR ID IGUAL contenido PUNTOYCOMA'

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
    | factor DIFERENTE factor'''

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
  print("Error de sintaxis: ",p)
# Construir parser

 

def sintactico():
  parser = sintaxis.yacc()

  while True:
      try:
          s = input(">")
      except EOFError:
          break
      if not s: continue
      result = parser.parse(s)
      print(result)