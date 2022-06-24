from fulvo.value import Number, String, BuiltInFunction
from fulvo.symbol_table import SymbolTable

######################################
# BUILT-IN CONST FUNCTIONS
######################################
global_symbol_table = SymbolTable()
global_symbol_table.set("NULL", Number.null)
global_symbol_table.set("FALSE", Number.false)
global_symbol_table.set("TRUE", Number.true)
global_symbol_table.set("MATH_PI", Number.math_PI)
global_symbol_table.set("D10S", String("Maradona"))
global_symbol_table.set("GOAT", String("Messi"))
global_symbol_table.set("MADRID", Number(912))
global_symbol_table.set("QATAR", Number(2022)) 
global_symbol_table.set("Relatar", BuiltInFunction("print"))
global_symbol_table.set("Relatar_ret", BuiltInFunction("print_ret"))
global_symbol_table.set("Poner", BuiltInFunction("input"))
global_symbol_table.set("Poner_numero", BuiltInFunction("input_int"))
global_symbol_table.set("Despejar", BuiltInFunction("clear"))
global_symbol_table.set("Salimoss", BuiltInFunction("clear"))
global_symbol_table.set("Es_Numero", BuiltInFunction("is_number"))
global_symbol_table.set("Es_String", BuiltInFunction("is_string"))
global_symbol_table.set("Es_Lista", BuiltInFunction("is_list"))
global_symbol_table.set("Es_Jugada", BuiltInFunction("is_function"))
global_symbol_table.set("Agregar", BuiltInFunction("append"))
global_symbol_table.set("Sacar", BuiltInFunction("pop"))
global_symbol_table.set("Extender", BuiltInFunction("extend"))
global_symbol_table.set("Longitud", BuiltInFunction("len"))
global_symbol_table.set("Arrancar_Partido", BuiltInFunction("run"))
######################################
#Estas me quedan por implementar
# global_symbol_table.set("Historico", BuiltInFunction("historico")) # gol a los ingleses
# global_symbol_table.set("Hacer_Falta", BuiltInFunction("falta"))
# global_symbol_table.set("Cabezaso", BuiltInFunction("cabezaso"))
# global_symbol_table.set("Ankara", BuiltInFunction("ankara"))
# global_symbol_table.set("Bicho", BuiltInFunction("bicho"))
# global_symbol_table.set("Boca", BuiltInFunction("boca"))
# global_symbol_table.set("River", BuiltInFunction("river"))

