import ply.yacc as sintaxis
import lexico as lex
tokens = lex.tokens

def p_sentencias(p):
    '''sentencias : variable
    | expresion
    | metodos
    '''

def p_metodos(p):
    '''metodos : imprimir
    | condi_anidado'''

#var _var; var a58a= ''; var _As=54;
def p_variable(p):
   '''variable : VAR ID PUNTOYCOMA
  | VAR ID IGUAL expresion PUNTOYCOMA
  | VAR ID IGUAL condi_anidado PUNTOYCOMA
  '''

#console.log('');
def p_imprimir(p):
  'imprimir : CONSOLE METODO LPAREN expresion RPAREN'

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
  '''condi_anidado : condicion AND  condi_anidado
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