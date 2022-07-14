from AnalizadorLexico import tokens, analizador

els = None
file = open('main.jf')
a = file.read()
program = a.split("\n")

# Prioridad de los tokens
procedence = (
    ('right', 'ASIGNACION'),
    ('right', 'IGUAL'),
    ('left', 'MAYORQUE', 'MANORQUE'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULTIPLICACION', 'DIVISION'),
    ('left', 'PARENTESIS_A', 'PARENTESIS_C'),
    ('left', 'LLAVE_A', 'LLAVE_C'), #mayor prioridad
)

nombres = {}


# produccion_nombre(t)
def p_init(t):
    '''init : instrucciones'''
    t[0] = t[1]


def p_instrucciones_lista(t):
    '''instrucciones : instrucciones instruccion'''
    t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones_instruccion(t):
    '''instrucciones : instruccion'''
    t[0] = [t[1]]


def p_instruccion(t):
    ''' instruccion : imprimir_instr
                    | asignacion_instr
                    | if_instr
                    | else_instr
                    | while_instr
    '''

    t[0] = t[1]



def p_if(t):
    '''if_instr : IF PARENTESIS_A expresion_logica PARENTESIS_C LLAVE_A statement LLAVE_C'''
    global els
    els = t[3]
    if (t[3]):
        t[0] = t[6]


def p_else(t):
    '''else_instr : ELSE LLAVE_A statement LLAVE_C'''
    if els != True:
        t[0] = t[3]
        print(t[3])


def p_statement(t):
    ''' statement : imprimir_instr
                    | if_instr
                    | expresion
                    | while_instr '''
    t[0] = t[1]


def p_while(t):
    '''while_instr : WHILE PARENTESIS_A expresion_logica PARENTESIS_C LLAVE_A statement LLAVE_C'''
    while (t[3]):
        t[0] = t[6]


# Asignacion de variables
def p_asignacion(t):
    'asignacion_instr : ID ASIGNACION expresion PUNTOCOMA'
    nombres[t[1]] = t[3]
    # print(nombres)


def p_asignacion_tipo(t):
    ''' expresion : ENTERO
                    | DECIMAL
                    | CADENA
    '''
    t[0] = t[1]


def p_expresion_id(t):
    ''' expresion : ID '''
    t[0] = nombres[t[1]]



# Funciones del lenguaje
def p_print(t):
    ''' imprimir_instr : IMPRIMIR PARENTESIS_A expresion PARENTESIS_C PUNTOCOMA
    '''
    t[0] = t[3]


def p_expresion_group(t):
    ''' expresion : PARENTESIS_A expresion PARENTESIS_C'''
    t[0] = t[2]


def p_expresion_logica(t):
    '''

        expresion_logica : expresion MENORQUE expresion
                         | expresion MAYORQUE expresion
                         | expresion IGUAL expresion
                         | expresion DIFERENTE expresion
                         | expresion MAYORIGUAL expresion
                         | expresion MENORIGUAL expresion
    '''
    if t[2] == '<':
        t[0] = t[1] < t[3]
    elif t[2] == '>':
        t[0] = t[1] > t[3]
    elif t[2] == '==':
        t[0] = t[1] == t[3]
    elif t[2] == '!=':
        t[0] = t[1] != t[3]
    elif t[2] == '<=':
        t[0] = t[1] <= t[3]
    elif t[2] == '>=':
        t[0] = t[1] >= t[3]


def p_expresion_logica_group(t):
    ''' expresion_logica : PARENTESIS_A expresion_logica PARENTESIS_C '''
    t[0] = t[2]


def p_expresion_logica_group(t):
    '''

        expresion_logica : PARENTESIS_A expresion_logica PARENTESIS_C MENORQUE PARENTESIS_A expresion_logica PARENTESIS_C
                         | PARENTESIS_A expresion_logica PARENTESIS_C MAYORQUE PARENTESIS_A expresion_logica PARENTESIS_C
                         | PARENTESIS_A expresion_logica PARENTESIS_C IGUAL PARENTESIS_A expresion_logica PARENTESIS_C
                         | PARENTESIS_A expresion_logica PARENTESIS_C DIFERENTE PARENTESIS_A expresion_logica PARENTESIS_C
                         | PARENTESIS_A expresion_logica PARENTESIS_C MAYORIGUAL PARENTESIS_A expresion_logica PARENTESIS_C
                         | PARENTESIS_A expresion_logica PARENTESIS_C MENORIGUAL PARENTESIS_A expresion_logica PARENTESIS_C
    '''

    if t[4] == '<':
        t[0] = t[2] < t[5]
    elif t[4] == '>':
        t[0] = t[2] > t[5]
    elif t[4] == '==':
        t[0] = t[2] == t[5]
    elif t[4] == '!=':
        t[0] = t[2] != t[5]
    elif t[2] == '<=':
        t[0] = t[2] <= t[5]
    elif t[2] == '>=':
        t[0] = t[2] >= t[5]


def p_expresion_operador_logico(t):
    '''expresion_logica : PARENTESIS_A expresion PARENTESIS_C AND PARENTESIS_A expresion_logica PARENTESIS_C
                        | PARENTESIS_A expresion PARENTESIS_C OR PARENTESIS_A expresion_logica PARENTESIS_C
                        | PARENTESIS_A expresion PARENTESIS_C NOT PARENTESIS_A expresion_logica PARENTESIS_C'''
    if t[4] == 'and':
        t[0] = t[2] and t[5]
    elif t[4] == 'or':
        t[0] = t[2] or t[5]
    elif t[4] == 'not':
        t[0] = t[2] is not t[5]


def p_expresion_operacion(t):
    '''
    expresion : expresion SUMA expresion
              | expresion RESTA expresion
              | expresion MULTIPLICACION expresion
              | expresion DIVISION expresion
    '''

    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]


def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintactico de tipo {} en el valor {}".format(str(t.type), str(t.value))
    else:
        resultado = "Error sintactico {}".format(t)
    resultado_gramatica.append(resultado)


import ply.yacc as yacc

parser = yacc.yacc()

resultado_gramatica = []


def prueba(data):
    resultado_gramatica.clear()
    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))

    return resultado_gramatica


def mostrarSintc(file):
    program = file.split("\n")
    for line in program:
        try:
            dato = eval(prueba(line)[0])[0]
            if dato is not None:
                print(dato)
        except:
            pass

#prueba
'''for line in program:
    try:
        dato = eval(prueba(line)[0])[0]
        if dato is not None:
            print(dato)
    except:
        pass'''
