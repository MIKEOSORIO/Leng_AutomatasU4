# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*- 
# -----------------------------------------------------------------------------
# Analizador léxico de JAVASCRIPT
# -----------------------------------------------------------------------------
# importa el primer módulo del ply
import ply.lex as lex
import codecs
import os
import re

from pip._vendor.distlib.compat import raw_input

tokens = [
    'MAYORIGUAL', 'MENORIGUAL', 'MENORQUE', 'MAYORQUE',
    'ILOGICO', 'OLOGICO', 'IGUALIGUAL', 'DIFERENTE',
    'LKEY', 'RKEY', 'LPAR', 'RPAR', 'LCOR', 'RCOR',
    'NEGBOOL', 'UMINUS', 'MEN', 'SUM', 'MULT', 'DIV', 'MOD', 'IGUAL', 'DOT', 'COMMA', 'DOTCOMMA',
    'ID', 'CAD', 'IDENTIFICADOR', 'NUMERO', 'ASIGNACION', 'IGUALACION', 'PLUS',
    'MINUS', 'DIVISION', 'DIVINVERSO', 'MULTIPLICACION',
    'MENORIGUALQUE', 'MAYORIGUALQUE', 'COMPARACION',
    'PARENTESISDER', 'PARENTESISIZQ', 'PUNTO', 'COMA', 'PUNTOCOMA', 'DOSPUNTOS',
    'COMILLASIMPLEDER', 'COMILLASIMPLEIZQ', 'COMILLADOBLEDER', 'COMSIMDER', 'COMSIMIZQ', 'COMDOBDER', 'COMDOIZQ',
    'COMENTARIO', 'COMMIT', 'FLOTANTES', 'BOOLEANO', 'NUM_ENTERO',
]

reservadas = {
    'return': 'RETURN',
    'this': 'THIS',
    'extends': 'EXTENDS',
    'if': 'IF',
    'new': 'NEW',
    'else': 'ELSE',
    'length': 'LENGTH',
    'int': 'INT',
    'while': 'WHILE',
    'true': 'TRUE',
    'boolean': 'BOOLEAN',
    'break': 'BREAK',
    'false': 'FALSE',
    'string': 'STRING',
    'continue': 'CONTINUE',
    'null': 'NULL',
    'case': 'CASE',
    'catch': 'CATCH',
    'const': 'CONST',
    'continue': 'CONTINUE',
    'break': 'BREAK',
    'delete': 'DELETE',
    'debugger': 'DEBUGGER',
    'do': 'DO',
    'else': 'ELSE',
    'finally': 'FINALLY',
    'for': 'FOR',
    'funtion': 'FUNTION',
    'if': 'IF',
    'in': 'IN',
    'instanceof': 'INSTANCEOF',
    'let': 'LET', 'new': 'NEW',
    'return': 'RETURN',
    'switch': 'SWITCH',
    'this': 'THIS',
    'throw': 'THROW',
    'try': 'TRY',
    'typeof': 'TYPEOF',
    'var': 'VAR',
    'void': 'VOID',
    'while': 'WHILE',
    'con': 'CON',
}
tokens = tokens + list(reservadas.values())

t_MAYORIGUAL = '>='
t_MENORIGUAL = '<='
t_MENORQUE = '<'
t_MAYORQUE = '>'
t_ILOGICO = '&&'
t_OLOGICO = r'\|\|'
t_IGUALIGUAL = r'=='
t_DIFERENTE = '!='
t_LKEY = '\{'
t_RKEY = '\}'
t_LPAR = '\('
t_RPAR = '\)'
t_LCOR = '\['
t_RCOR = r'\]'
t_NEGBOOL = '!'
t_MEN = '-'
t_UMINUS = '\-'
t_SUM = '\+'
t_MULT = '\*'
t_DIV = r'/'
t_MOD = '%'
t_IGUAL = '='
t_DOT = r'\.'
t_COMMA = ','
t_DOTCOMMA = ';'
t_DOSPUNTOS = r':'
t_COMSIMDER = r'\''
t_COMSIMIZQ = r'\''
t_COMDOBDER = r'\"'
t_COMDOIZQ = r'\"'
t_ignore_COMENTARIO = '\/\/.*'


def t_COMENTARIO(t):
    r'(/\*(.|\n|\r|\t)*?\*/)|//.*'
    return t


def t_COMMIT(t):
    r'(<!--)[a-zA-Z_]*( )*[\w]*'
    return t


# BINARIO-----------------------------------------------
def t_BINARIO(t):
    r'[b]\'[01]+\''
    t.value = int(t.value[2:-1], 2)
    return t

def t_BREAK(t):
    r'break'
    return t


def BOOLEAN(t):
    r'boolean'
    return t


def ELSE(t):
    r'else'
    return t


def NULL(t):
    r'null'
    return t


def DEBUGGER(t):
    r'debugger'
    return t

def t_BOOLEANO(t):
    r'(false|true)'
    return t

def t_RETURN(t):
    r'return'
    return t


def t_DO(t):
    r'do'
    return t


def t_WHILE(t):
    r'while'
    return t

def t_NEW(t):
    r'new'
    return t


def t_ELSE(t):
    r'else'
    return t


def t_LENGTH(t):
    r'length'
    return t


def t_INT(t):
    r'int'
    return t


def t_FINALLY(t):
    r'finally'
    return t


def t_FOR(t):
    r'for'
    return t

def FOR(t):
    r'for'
    return t


def CONST(t):
    r'const'
    return t

def t_VAR(t):
    r'([A-Za-z_]){1,}\w+[\s,\S]\='
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_CAD(t):
    r'"([\x19-\x7E]|\t|\r)*"'
    return t

def t_error_CAD(t):
    r'"([\x20-\x7E]|\\\\|\\n|\\t|\\r)*'
    print("Inicio de una cadena/la cadena no quedo bien cerrada")

def t_FLOTANTES(t): #numeros flotantes positivos y negativos
    r'(\d+\.\d+|-\d+\.\d+)'
    return t

def t_NUM_ENTERO(t): #numeros enteros negativos y positivos
    r'[+,-]?[0-9]{1,}'
    t.value = int(t.value)
    return t



t_ignore = " \t"  # ignorando el espacio


# NEWLINE----------------------------------------------
# reconoce un salto de linea y cuenta los saltos de linea para saber cuantas lineas hay
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


# ERROR------------------------------------------------
# entra aca si no concuerda con ningun caracter, es decir si no reconoce un token
def t_error(t):
    print("No se reconoce el caracter '%s'" % t.value[0])
    t.lexer.skip(1)  # salta para que el analizador siga reconociendo mas
    t.value = str(t.value)


# buscarFicheros---------------------------------------
def buscarFicheros(directoriomio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1

    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)

    for file in files:
        print(str(cont) + ". " + file)
        cont = cont + 1

    while respuesta == False:
        numArchivo = raw_input('\nNumero del Test: ')
        for file in files:
            if file == files[int(numArchivo) - 1]:
                respuesta = True
                break

    print("Has escogido \"%s\" \n" % files[int(numArchivo) - 1])
    return files[int(numArchivo) - 1]


#--------------------------------------------------------------------------------------------------------
# 5. Construye el analizador
analizador = lex.lex()  # coge todos los automatas y los junta en uno sol

print("\nBienvenido al Analizador Lexico.")
print("Por favor, elige la prueba")

directorio = "C:/Users/Miguel_Cupul/Desktop/Analizador_Lexico/Pruebas/"
archivo = buscarFicheros(directorio)
test = directorio + archivo
fp = codecs.open(test, "r", encoding= 'utf-8')
cadena = fp.read()
cadena = str(cadena)
fp.close()

analizador.input(cadena)

# Muestra la lista de tokens
print("\nToken  |   Lexema   |   Línea   |   Número de Carácter Empieza\n")
while True:
    tok = analizador.token()
    if not tok: break  # fin de la lista
    print(tok)
print("\n\n", "Equipo:\n", "Miguel Angel Cupul Osorio\n", "Wilbert Jesus del Valle Sierra\n", "Marcos Ricardo Ochoa Castillo" )
