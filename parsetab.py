
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND COMA COMILLA COMILLITA COMPARADOR CONSOLE DIFERENTE DIVIDE DOSPUNTOS ELIF ELSE FOR ID IF IGUAL IGUALA INDECREMENTAL LCORCH LLLAVE LPAREN METODO MINUS NEW NOT NUMBER OPERADORES OR PLUS POTENCIA PROMPT PUNTO PUNTOYCOMA RCORCH RLLAVE RPAREN SET TEXTO TIMES VAR WHILEsentencias : variable sentencias\n    | expresion sentencias\n    | metodos sentencias\n    | iteracion sentencias\n    | objeto PUNTOYCOMA sentencias\n    | newset sentencias\n    | array sentencias\n    | empty\n    metodos : imprimir PUNTOYCOMA\n    | condi_anidado\n    | metodo PUNTOYCOMAvariable : VAR ID PUNTOYCOMA\n  | VAR ID IGUAL expresion PUNTOYCOMA\n  | VAR ID IGUAL condi_anidado PUNTOYCOMA\n  iteracion : FOR LPAREN ID IGUAL NUMBER PUNTOYCOMA condicion PUNTOYCOMA ID INDECREMENTAL RPAREN LLLAVE sentencias RLLAVEimprimir : CONSOLE METODO LPAREN expresion RPARENmetodo : ID METODO LPAREN RPARENmetodo : ID METODO LPAREN expresion RPARENmetodo : ID METODO LPAREN expresion COMA expresion RPARENmetodo : ID METODOobjeto : VAR ID IGUAL LLLAVE RLLAVE  \n  | VAR ID IGUAL LLLAVE keyvalue RLLAVE   \n  keyvalue : ID DOSPUNTOS factor COMA keyvalue\n  | ID DOSPUNTOS factor COMA\n  newset : VAR ID IGUAL NEW SET LPAREN RPAREN PUNTOYCOMA\n  | VAR ID IGUAL NEW SET LPAREN contenido RPAREN PUNTOYCOMAarray : VAR ID IGUAL contenido PUNTOYCOMAcontenido : LCORCH elemento RCORCH\n  | LCORCH RCORCH\n  | LCORCH expresion RCORCHelemento : expresion \n  | expresion COMA elemento expresion : expresion PLUS factorexpresion : expresion MINUS termexpresion : expresion TIMES termexpresion : expresion DIVIDE termexpresion : expresion POTENCIA termexpresion : termcondi_anidado : condicion AND condi_anidado\n  | NOT condicion AND  condi_anidado \n  | condicion OR  condi_anidado\n  | NOT condicion OR  condi_anidado\n  | condicion \n  | NOT condicion condicion : factor COMPARADOR factor\n    | factor IGUALA factor\n    | factor DIFERENTE factorterm : factorfactor : LPAREN expresion RPARENfactor : NUMBERfactor : TEXTOfactor : IDempty :'
    
_lr_action_items = {'VAR':([0,2,3,4,5,7,8,11,12,13,14,19,20,23,33,41,42,45,46,50,52,53,54,55,56,58,61,62,63,65,66,67,81,82,83,84,89,113,117,121,123,],[10,10,10,10,10,10,10,-52,-10,-48,-38,-50,-43,-51,10,-9,-11,-48,-52,-44,-33,-34,-35,-36,-37,-12,-45,-46,-47,-49,-39,-41,-40,-42,-13,-14,-27,-25,-26,10,-15,]),'FOR':([0,2,3,4,5,7,8,11,12,13,14,19,20,23,33,41,42,45,46,50,52,53,54,55,56,58,61,62,63,65,66,67,81,82,83,84,89,113,117,121,123,],[17,17,17,17,17,17,17,-52,-10,-48,-38,-50,-43,-51,17,-9,-11,-48,-52,-44,-33,-34,-35,-36,-37,-12,-45,-46,-47,-49,-39,-41,-40,-42,-13,-14,-27,-25,-26,17,-15,]),'$end':([0,1,2,3,4,5,7,8,9,11,12,13,14,19,20,23,24,25,31,32,33,34,35,41,42,45,46,50,52,53,54,55,56,57,58,61,62,63,65,66,67,81,82,83,84,89,113,117,123,],[-53,0,-53,-53,-53,-53,-53,-53,-8,-52,-10,-48,-38,-50,-43,-51,-1,-2,-3,-4,-53,-6,-7,-9,-11,-48,-52,-44,-33,-34,-35,-36,-37,-5,-12,-45,-46,-47,-49,-39,-41,-40,-42,-13,-14,-27,-25,-26,-15,]),'CONSOLE':([0,2,3,4,5,7,8,11,12,13,14,19,20,23,33,41,42,45,46,50,52,53,54,55,56,58,61,62,63,65,66,67,81,82,83,84,89,113,117,121,123,],[21,21,21,21,21,21,21,-52,-10,-48,-38,-50,-43,-51,21,-9,-11,-48,-52,-44,-33,-34,-35,-36,-37,-12,-45,-46,-47,-49,-39,-41,-40,-42,-13,-14,-27,-25,-26,21,-15,]),'NOT':([0,2,3,4,5,7,8,11,12,13,14,19,20,23,33,41,42,45,46,47,48,50,52,53,54,55,56,58,59,61,62,63,65,66,67,69,70,81,82,83,84,89,113,117,121,123,],[22,22,22,22,22,22,22,-52,-10,-48,-38,-50,-43,-51,22,-9,-11,-48,-52,22,22,-44,-33,-34,-35,-36,-37,-12,22,-45,-46,-47,-49,-39,-41,22,22,-40,-42,-13,-14,-27,-25,-26,22,-15,]),'ID':([0,2,3,4,5,7,8,10,11,12,13,14,18,19,20,22,23,26,27,28,29,30,33,38,39,40,41,42,43,45,46,47,48,50,52,53,54,55,56,58,59,60,61,62,63,65,66,67,68,69,70,73,76,81,82,83,84,89,94,97,102,104,112,113,115,117,121,123,],[11,11,11,11,11,11,11,36,-52,-10,-48,-38,46,-50,-43,46,-51,46,46,46,46,46,11,46,46,46,-9,-11,64,-48,-52,46,46,-44,-33,-34,-35,-36,-37,-12,46,46,-45,-46,-47,-49,-39,-41,46,46,46,85,46,-40,-42,-13,-14,-27,46,46,46,46,85,-25,118,-26,11,-15,]),'LPAREN':([0,2,3,4,5,7,8,11,12,13,14,17,18,19,20,22,23,26,27,28,29,30,33,37,38,39,40,41,42,45,46,47,48,49,50,52,53,54,55,56,58,59,60,61,62,63,65,66,67,68,69,70,76,81,82,83,84,88,89,94,97,102,104,113,117,121,123,],[18,18,18,18,18,18,18,-52,-10,-48,-38,43,18,-50,-43,18,-51,18,18,18,18,18,18,60,18,18,18,-9,-11,-48,-52,18,18,68,-44,-33,-34,-35,-36,-37,-12,18,18,-45,-46,-47,-49,-39,-41,18,18,18,18,-40,-42,-13,-14,99,-27,18,18,18,18,-25,-26,18,-15,]),'NUMBER':([0,2,3,4,5,7,8,11,12,13,14,18,19,20,22,23,26,27,28,29,30,33,38,39,40,41,42,45,46,47,48,50,52,53,54,55,56,58,59,60,61,62,63,65,66,67,68,69,70,76,79,81,82,83,84,89,94,97,102,104,113,117,121,123,],[19,19,19,19,19,19,19,-52,-10,-48,-38,19,-50,-43,19,-51,19,19,19,19,19,19,19,19,19,-9,-11,-48,-52,19,19,-44,-33,-34,-35,-36,-37,-12,19,19,-45,-46,-47,-49,-39,-41,19,19,19,19,95,-40,-42,-13,-14,-27,19,19,19,19,-25,-26,19,-15,]),'TEXTO':([0,2,3,4,5,7,8,11,12,13,14,18,19,20,22,23,26,27,28,29,30,33,38,39,40,41,42,45,46,47,48,50,52,53,54,55,56,58,59,60,61,62,63,65,66,67,68,69,70,76,81,82,83,84,89,94,97,102,104,113,117,121,123,],[23,23,23,23,23,23,23,-52,-10,-48,-38,23,-50,-43,23,-51,23,23,23,23,23,23,23,23,23,-9,-11,-48,-52,23,23,-44,-33,-34,-35,-36,-37,-12,23,23,-45,-46,-47,-49,-39,-41,23,23,23,23,-40,-42,-13,-14,-27,23,23,23,23,-25,-26,23,-15,]),'RLLAVE':([2,3,4,5,7,8,9,11,12,13,14,19,20,23,24,25,31,32,33,34,35,41,42,45,46,50,52,53,54,55,56,57,58,61,62,63,65,66,67,73,81,82,83,84,87,89,112,113,116,117,121,122,123,],[-53,-53,-53,-53,-53,-53,-8,-52,-10,-48,-38,-50,-43,-51,-1,-2,-3,-4,-53,-6,-7,-9,-11,-48,-52,-44,-33,-34,-35,-36,-37,-5,-12,-45,-46,-47,-49,-39,-41,86,-40,-42,-13,-14,98,-27,-24,-25,-23,-26,-53,123,-15,]),'PLUS':([3,11,13,14,19,23,44,45,46,52,53,54,55,56,65,71,78,80,92,103,108,],[26,-52,-48,-38,-50,-51,26,-48,-52,-33,-34,-35,-36,-37,-49,26,26,26,26,26,26,]),'MINUS':([3,11,13,14,19,23,44,45,46,52,53,54,55,56,65,71,78,80,92,103,108,],[27,-52,-48,-38,-50,-51,27,-48,-52,-33,-34,-35,-36,-37,-49,27,27,27,27,27,27,]),'TIMES':([3,11,13,14,19,23,44,45,46,52,53,54,55,56,65,71,78,80,92,103,108,],[28,-52,-48,-38,-50,-51,28,-48,-52,-33,-34,-35,-36,-37,-49,28,28,28,28,28,28,]),'DIVIDE':([3,11,13,14,19,23,44,45,46,52,53,54,55,56,65,71,78,80,92,103,108,],[29,-52,-48,-38,-50,-51,29,-48,-52,-33,-34,-35,-36,-37,-49,29,29,29,29,29,29,]),'POTENCIA':([3,11,13,14,19,23,44,45,46,52,53,54,55,56,65,71,78,80,92,103,108,],[30,-52,-48,-38,-50,-51,30,-48,-52,-33,-34,-35,-36,-37,-49,30,30,30,30,30,30,]),'PUNTOYCOMA':([6,13,14,15,16,19,20,23,36,37,45,46,50,52,53,54,55,56,61,62,63,65,66,67,71,72,75,77,81,82,86,91,93,95,96,98,100,101,106,110,111,114,],[33,-48,-38,41,42,-50,-43,-51,58,-20,-48,-52,-44,-33,-34,-35,-36,-37,-45,-46,-47,-49,-39,-41,83,84,89,-17,-40,-42,-21,-29,-18,104,-16,-22,-28,-30,113,-19,115,117,]),'METODO':([11,21,],[37,49,]),'COMPARADOR':([11,13,19,23,46,51,65,],[-52,38,-50,-51,-52,38,-49,]),'IGUALA':([11,13,19,23,46,51,65,],[-52,39,-50,-51,-52,39,-49,]),'DIFERENTE':([11,13,19,23,46,51,65,],[-52,40,-50,-51,-52,40,-49,]),'RPAREN':([14,19,23,44,45,46,52,53,54,55,56,60,65,78,80,91,99,100,101,103,107,119,],[-38,-50,-51,65,-48,-52,-33,-34,-35,-36,-37,77,-49,93,96,-29,106,-28,-30,110,114,120,]),'COMA':([14,19,23,45,46,52,53,54,55,56,65,78,92,105,108,],[-38,-50,-51,-48,-52,-33,-34,-35,-36,-37,-49,94,102,112,102,]),'RCORCH':([14,19,23,45,46,52,53,54,55,56,65,76,90,92,108,109,],[-38,-50,-51,-48,-52,-33,-34,-35,-36,-37,-49,91,100,101,-31,-32,]),'AND':([19,20,23,46,50,61,62,63,65,],[-50,47,-51,-52,69,-45,-46,-47,-49,]),'OR':([19,20,23,46,50,61,62,63,65,],[-50,48,-51,-52,70,-45,-46,-47,-49,]),'IGUAL':([36,64,],[59,79,]),'LLLAVE':([59,120,],[73,121,]),'NEW':([59,],[74,]),'LCORCH':([59,99,],[76,76,]),'SET':([74,],[88,]),'DOSPUNTOS':([85,],[97,]),'INDECREMENTAL':([118,],[119,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sentencias':([0,2,3,4,5,7,8,33,121,],[1,24,25,31,32,34,35,57,122,]),'variable':([0,2,3,4,5,7,8,33,121,],[2,2,2,2,2,2,2,2,2,]),'expresion':([0,2,3,4,5,7,8,18,33,59,60,68,76,94,102,121,],[3,3,3,3,3,3,3,44,3,71,78,80,92,103,108,3,]),'metodos':([0,2,3,4,5,7,8,33,121,],[4,4,4,4,4,4,4,4,4,]),'iteracion':([0,2,3,4,5,7,8,33,121,],[5,5,5,5,5,5,5,5,5,]),'objeto':([0,2,3,4,5,7,8,33,121,],[6,6,6,6,6,6,6,6,6,]),'newset':([0,2,3,4,5,7,8,33,121,],[7,7,7,7,7,7,7,7,7,]),'array':([0,2,3,4,5,7,8,33,121,],[8,8,8,8,8,8,8,8,8,]),'empty':([0,2,3,4,5,7,8,33,121,],[9,9,9,9,9,9,9,9,9,]),'condi_anidado':([0,2,3,4,5,7,8,33,47,48,59,69,70,121,],[12,12,12,12,12,12,12,12,66,67,72,81,82,12,]),'factor':([0,2,3,4,5,7,8,18,22,26,27,28,29,30,33,38,39,40,47,48,59,60,68,69,70,76,94,97,102,104,121,],[13,13,13,13,13,13,13,45,51,52,45,45,45,45,13,61,62,63,51,51,13,45,45,51,51,45,45,105,45,51,13,]),'term':([0,2,3,4,5,7,8,18,27,28,29,30,33,59,60,68,76,94,102,121,],[14,14,14,14,14,14,14,14,53,54,55,56,14,14,14,14,14,14,14,14,]),'imprimir':([0,2,3,4,5,7,8,33,121,],[15,15,15,15,15,15,15,15,15,]),'metodo':([0,2,3,4,5,7,8,33,121,],[16,16,16,16,16,16,16,16,16,]),'condicion':([0,2,3,4,5,7,8,22,33,47,48,59,69,70,104,121,],[20,20,20,20,20,20,20,50,20,20,20,20,20,20,111,20,]),'contenido':([59,99,],[75,107,]),'keyvalue':([73,112,],[87,116,]),'elemento':([76,102,],[90,109,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sentencias","S'",1,None,None,None),
  ('sentencias -> variable sentencias','sentencias',2,'p_sentencias','sintactico.py',7),
  ('sentencias -> expresion sentencias','sentencias',2,'p_sentencias','sintactico.py',8),
  ('sentencias -> metodos sentencias','sentencias',2,'p_sentencias','sintactico.py',9),
  ('sentencias -> iteracion sentencias','sentencias',2,'p_sentencias','sintactico.py',10),
  ('sentencias -> objeto PUNTOYCOMA sentencias','sentencias',3,'p_sentencias','sintactico.py',11),
  ('sentencias -> newset sentencias','sentencias',2,'p_sentencias','sintactico.py',12),
  ('sentencias -> array sentencias','sentencias',2,'p_sentencias','sintactico.py',13),
  ('sentencias -> empty','sentencias',1,'p_sentencias','sintactico.py',14),
  ('metodos -> imprimir PUNTOYCOMA','metodos',2,'p_metodos','sintactico.py',18),
  ('metodos -> condi_anidado','metodos',1,'p_metodos','sintactico.py',19),
  ('metodos -> metodo PUNTOYCOMA','metodos',2,'p_metodos','sintactico.py',20),
  ('variable -> VAR ID PUNTOYCOMA','variable',3,'p_variable','sintactico.py',24),
  ('variable -> VAR ID IGUAL expresion PUNTOYCOMA','variable',5,'p_variable','sintactico.py',25),
  ('variable -> VAR ID IGUAL condi_anidado PUNTOYCOMA','variable',5,'p_variable','sintactico.py',26),
  ('iteracion -> FOR LPAREN ID IGUAL NUMBER PUNTOYCOMA condicion PUNTOYCOMA ID INDECREMENTAL RPAREN LLLAVE sentencias RLLAVE','iteracion',14,'p_for','sintactico.py',31),
  ('imprimir -> CONSOLE METODO LPAREN expresion RPAREN','imprimir',5,'p_imprimir','sintactico.py',35),
  ('metodo -> ID METODO LPAREN RPAREN','metodo',4,'p_metodo_argumento0','sintactico.py',39),
  ('metodo -> ID METODO LPAREN expresion RPAREN','metodo',5,'p_metodo_argumento1','sintactico.py',42),
  ('metodo -> ID METODO LPAREN expresion COMA expresion RPAREN','metodo',7,'p_metodo_argumento2','sintactico.py',45),
  ('metodo -> ID METODO','metodo',2,'p_metodo_argumento3','sintactico.py',49),
  ('objeto -> VAR ID IGUAL LLLAVE RLLAVE','objeto',5,'p_objeto','sintactico.py',53),
  ('objeto -> VAR ID IGUAL LLLAVE keyvalue RLLAVE','objeto',6,'p_objeto','sintactico.py',54),
  ('keyvalue -> ID DOSPUNTOS factor COMA keyvalue','keyvalue',5,'p_objeto_kv','sintactico.py',58),
  ('keyvalue -> ID DOSPUNTOS factor COMA','keyvalue',4,'p_objeto_kv','sintactico.py',59),
  ('newset -> VAR ID IGUAL NEW SET LPAREN RPAREN PUNTOYCOMA','newset',8,'p_set','sintactico.py',63),
  ('newset -> VAR ID IGUAL NEW SET LPAREN contenido RPAREN PUNTOYCOMA','newset',9,'p_set','sintactico.py',64),
  ('array -> VAR ID IGUAL contenido PUNTOYCOMA','array',5,'p_array','sintactico.py',67),
  ('contenido -> LCORCH elemento RCORCH','contenido',3,'p_contenido','sintactico.py',70),
  ('contenido -> LCORCH RCORCH','contenido',2,'p_contenido','sintactico.py',71),
  ('contenido -> LCORCH expresion RCORCH','contenido',3,'p_contenido','sintactico.py',72),
  ('elemento -> expresion','elemento',1,'p_elemento','sintactico.py',75),
  ('elemento -> expresion COMA elemento','elemento',3,'p_elemento','sintactico.py',76),
  ('expresion -> expresion PLUS factor','expresion',3,'p_expresion_suma','sintactico.py',86),
  ('expresion -> expresion MINUS term','expresion',3,'p_expresion_resta','sintactico.py',90),
  ('expresion -> expresion TIMES term','expresion',3,'p_expresion_producto','sintactico.py',93),
  ('expresion -> expresion DIVIDE term','expresion',3,'p_expresion_division','sintactico.py',96),
  ('expresion -> expresion POTENCIA term','expresion',3,'p_expresion_potencia','sintactico.py',99),
  ('expresion -> term','expresion',1,'p_expression_term','sintactico.py',102),
  ('condi_anidado -> condicion AND condi_anidado','condi_anidado',3,'p_condicion_operador','sintactico.py',106),
  ('condi_anidado -> NOT condicion AND condi_anidado','condi_anidado',4,'p_condicion_operador','sintactico.py',107),
  ('condi_anidado -> condicion OR condi_anidado','condi_anidado',3,'p_condicion_operador','sintactico.py',108),
  ('condi_anidado -> NOT condicion OR condi_anidado','condi_anidado',4,'p_condicion_operador','sintactico.py',109),
  ('condi_anidado -> condicion','condi_anidado',1,'p_condicion_operador','sintactico.py',110),
  ('condi_anidado -> NOT condicion','condi_anidado',2,'p_condicion_operador','sintactico.py',111),
  ('condicion -> factor COMPARADOR factor','condicion',3,'p_condicion','sintactico.py',116),
  ('condicion -> factor IGUALA factor','condicion',3,'p_condicion','sintactico.py',117),
  ('condicion -> factor DIFERENTE factor','condicion',3,'p_condicion','sintactico.py',118),
  ('term -> factor','term',1,'p_term_factor','sintactico.py',121),
  ('factor -> LPAREN expresion RPAREN','factor',3,'p_factor_expr','sintactico.py',124),
  ('factor -> NUMBER','factor',1,'p_factor_num','sintactico.py',127),
  ('factor -> TEXTO','factor',1,'p_factor_str','sintactico.py',130),
  ('factor -> ID','factor',1,'p_factor_var2','sintactico.py',133),
  ('empty -> <empty>','empty',0,'p_empty','sintactico.py',137),
]
