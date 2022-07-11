import ply.lex as lex

file = open('main.jf')
a = file.read()
program = a.split("\n")

tokens = [
    'ID',
    'NUMERO',
    'SUMA',
    'ASIGNACION',
    'RESTA',
    'DIVISION',
    'MULTIPLICACION',

    'IGUAL',
    'DIFERENTE',
    'MAYORQUE',
    'MENORQUE',
    'MENORIGUAL',
    'MAYORIGUAL',

    'PUNTO',
    'COMA',
    'DOSPUNTOS',
    'PUNTOCOMA',
    'COMILLASIMPLE',
    'COMILLADOBLE',
    'PARENTESIS_A',
    'PARENTESIS_C',
    'LLAVE_A',
    'LLAVE_C',
    'CORCHETE_A',
    'CORCHETE_C',
    'CADENA',
    'COMENTARIO',

    'MASMAS',
    'MENOSMENOS'
]

reservadas = {
    'import': 'IMPORT',
    'def': 'DEF',
    'class': 'CLASS',
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'in': 'IN',
    'range': 'RANGE',
    'self': 'SELF',
    'while': 'WHILE',
    'try': 'TRY',
    'except': 'EXCEPT',
    'return': 'RETURN',
    'break': 'BREAK',
    'next': 'NEXT',

    'input': 'LEER',
    'print': 'IMPRIMIR',
    'int': 'ENTERO',
    'float': 'DECIMAL',
    'boolean': 'BOOLEAN',

    'pow': 'POTENCIA',
    'math.srq': 'RAIZ',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT'
}

tokens = tokens + list(reservadas.values())

t_ignore = '\t '

# OPERADORRES MATEMATICOS
t_SUMA = r'\+'
t_ASIGNACION = r'='
t_RESTA = r'\-'
t_DIVISION = r'/'
t_MULTIPLICACION = r'\*'

# OPERADORES RACIONALES
t_IGUAL = r'=='
t_DIFERENTE = r'!='
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='

# VARIABLES
# t_IDENTIFICADOR=exprecion regular
t_PUNTO = r'\.'
t_COMA = r'\,'
t_DOSPUNTOS = r'\:'
t_PUNTOCOMA = r'\;'
t_COMILLASIMPLE = r'\''
t_COMILLADOBLE = r'\"'
t_PARENTESIS_A = r'\('
t_PARENTESIS_C = r'\)'
t_LLAVE_A = r'\{'
t_LLAVE_C = r'\}'
t_CORCHETE_A = r'\['
t_CORCHETE_C = r'\]'

# OPERADORES DE DECRECIMIENTO E INCREMENTO
t_MASMAS = r'\+\+'
t_MENOSMENOS = r'\-\-'
t_IMPRIMIR=r'print'
t_OR=r'or'
t_AND=r'and'
t_NOT=r'not'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    #if t.value.upper() in reservadas:
       # t.value = t.value.upper()
        #t.type = t.value
    t.type=reservadas.get(t.value.lower(),'ID')
    return t


def t_SALTOLINEA(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_COMENTARIO(t):
    r'\#.*'
    pass


def t_ENTERO(t):
    r'\d+'
    try:
        t.value=int(t.value)
    except ValueError:
        print("Integer value too large %d",t.value)
        t.value=0
    return t


def t_error(t):
    print("caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)
    return t


def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

def t_DECIMAL(t):
    r'(\d*\.\d+)|(\d+\-\d*)'
    try:
        t.value=float(t.value)
    except ValueError:
        print("Float value too large %d ",t.value)
        t.value=0
    return t



a = []


#def analisis(cadena):
#    analizador = lex.lex()
 #   analizador.input(cadena)
#    a.clear()
 #   while True:
 #       tok = analizador.token()
#        if not tok: break
#        a.append(str(tok))
#    return a


#contador = 1
#for line in program:
   # data = analisis(line)
   # print(f"-------------------Linea#{contador}-------------------")
    #for dato in data:
  #      print(dato)
  #  contador += 1


analizador=lex.lex()
