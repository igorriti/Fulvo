from fulvo.error import RTError
from fulvo.RTResult import RTResult
from fulvo.context import Context
from fulvo.symbol_table import SymbolTable
from fulvo.basic import *
from fulvo.dios.vid_to_ascii import *

import math
import os
from time import sleep
import sys


#######################################
# VALUES
#######################################

class Value:
	def __init__(self):
		self.set_pos()
		self.set_context()

	def set_pos(self, pos_start=None, pos_end=None):
		self.pos_start = pos_start
		self.pos_end = pos_end
		return self

	def set_context(self, context=None):
		self.context = context
		return self

	def added_to(self, other):
		return None, self.illegal_operation(other)

	def subbed_by(self, other):
		return None, self.illegal_operation(other)

	def multed_by(self, other):
		return None, self.illegal_operation(other)

	def dived_by(self, other):
		return None, self.illegal_operation(other)

	def powed_by(self, other):
		return None, self.illegal_operation(other)

	def get_comparison_eq(self, other):
		return None, self.illegal_operation(other)

	def get_comparison_ne(self, other):
		return None, self.illegal_operation(other)

	def get_comparison_lt(self, other):
		return None, self.illegal_operation(other)

	def get_comparison_gt(self, other):
		return None, self.illegal_operation(other)

	def get_comparison_lte(self, other):
		return None, self.illegal_operation(other)

	def get_comparison_gte(self, other):
		return None, self.illegal_operation(other)

	def anded_by(self, other):
		return None, self.illegal_operation(other)

	def ored_by(self, other):
		return None, self.illegal_operation(other)

	def notted(self, other):
		return None, self.illegal_operation(other)

	def execute(self, args):
		return RTResult().failure(self.illegal_operation())

	def copy(self):
		raise Exception('No copy method defined')

	def is_true(self):
		return False

	def __str__(self):
		return str(self.value)
	
	def illegal_operation(self, other=None):
		if not other: other = self
		return RTError(
			self.pos_start, other.pos_end,
			'Illegal operation',
			self.context
		)

class Number(Value):
	def __init__(self, value):
		super().__init__()
		self.value = value
	
	def added_to(self, other):
		if isinstance(other, Number):
			return Number(self.value + other.value).set_context(self.context), None
		else:
			return None, Value.illegal_operation(self, other)

	def subbed_by(self, other):
		if isinstance(other, Number):
			return Number(self.value - other.value).set_context(self.context), None
		else:
			return None, Value.illegal_operation(self, other)

	def multed_by(self, other):
		if isinstance(other, Number):
			return Number(self.value * other.value).set_context(self.context), None
		else:
			return None, Value.illegal_operation(self, other)

	def dived_by(self, other):
		if isinstance(other, Number):
			if other.value == 0:
				return None, RTError(
					other.pos_start, other.pos_end,
					'Es mas posible que San Marino gane un partido a que puedas dividir por 0',
					self.context
				)

			return Number(self.value / other.value).set_context(self.context), None
		else:
			return None, Value.illegal_operation(self, other)

	def powed_by(self, other):
		if isinstance(other, Number):
			return Number(self.value ** other.value).set_context(self.context), None
		else:
			return None, Value.illegal_operation(self, other)

	def get_comparison_eq(self, other):
		if isinstance(other, Number):
			return Number(int(self.value == other.value)).set_context(self.context), None
		else:
			return None, Value.illegal_operation(self, other)

	def get_comparison_ne(self, other):
		if isinstance(other, Number):
			return Number(int(self.value != other.value)).set_context(self.context), None
		else:
			return None, Value.illegal_operation(self, other)

	def get_comparison_lt(self, other):
		if isinstance(other, Number):
			return Number(int(self.value < other.value)).set_context(self.context), None
		else:
			return None, Value.illegal_operation(self, other)

	def get_comparison_gt(self, other):
		if isinstance(other, Number):
			return Number(int(self.value > other.value)).set_context(self.context), None
		else:
			return None, Value.illegal_operation(self, other)

	def get_comparison_lte(self, other):
		if isinstance(other, Number):
			return Number(int(self.value <= other.value)).set_context(self.context), None
		else:
			return None, Value.illegal_operation(self, other)

	def get_comparison_gte(self, other):
		if isinstance(other, Number):
			return Number(int(self.value >= other.value)).set_context(self.context), None
		else:
			return None, Value.illegal_operation(self, other)

	def anded_by(self, other):
		if isinstance(other, Number):
			return Number(int(self.value and other.value)).set_context(self.context), None
		else:
			return None, Value.illegal_operation(self, other)

	def ored_by(self, other):
		if isinstance(other, Number):
			return Number(int(self.value or other.value)).set_context(self.context), None
		else:
			return None, Value.illegal_operation(self, other)

	def notted(self):
		return Number(1 if self.value == 0 else 0).set_context(self.context), None

	def copy(self):
		copy = Number(self.value)
		copy.set_pos(self.pos_start, self.pos_end)
		copy.set_context(self.context)
		return copy

	def is_true(self):
		return self.value != 0
	
	def __repr__(self):
		return str(self.value)

Number.null = Number(0)
Number.false = Number(0)
Number.true = Number(1)
Number.math_PI = Number(math.pi)

class String(Value):
	def __init__(self, value):
		super().__init__()
		self.value = value

	def added_to(self, other):
		if isinstance(other, String):
			return String(self.value + other.value).set_context(self.context), None
		else:
			return None, Value.illegal_operation(self, other)
	
	def multed_by(self, other):
		if isinstance(other, Number):
			return String(self.value * other.value).set_context(self.context), None
		else:
			return None, Value.illegal_operation(self, other)
	
	def is_true(self):
		return len(self.value) > 0

	def copy(self):
		copy = String(self.value)
		copy.set_pos(self.pos_start, self.pos_end)
		copy.set_context(self.context)
		return copy
	
	def __str__(self):
		return self.value

	def __repr__(self):
		return f'"{self.value}"'

class List(Value):
	def __init__(self, elements):
		super().__init__()
		self.elements = elements

	def added_to(self, other):
		new_list = self.copy()
		new_list.elements.append(other)
		return new_list, None

	def subbed_by(self, other):
		if isinstance(other, Number):
			new_list = self.copy()
			try:
				new_list.elements.pop(other.value)
				return new_list, None
			except:
				return None, RTError(
					other.pos_start, other.pos_end,
					'No se puede eliminar un elemento de una lista que no existe',
					self.context
				)
		else:
			return None, Value.illegal_operation(self, other)

	def multed_by(self, other):
		if isinstance(other, List):
			new_list = self.copy()
			new_list.elements.extend(other.elements)
			return new_list, None
		else:
			return None, Value.illegal_operation(self, other)

	def dived_by(self, other):
		if isinstance(other, Number):
			try:
				return self.elements[other.value], None
			except:
				return None, RTError(
					other.pos_start, other.pos_end,
					'No se puede obtener un elemento de una lista que no existe',
					self.context
				)
		else:
			return None, Value.illegal_operation(self, other)

	def copy(self):
		copy = List(self.elements)
		copy.set_pos(self.pos_start, self.pos_end)
		copy.set_context(self.context)
		return copy

	def __str__(self):
		return ", ".join(str(x) for x in self.elements)
	def __repr__(self):
		return f'[{", ".join(str(x) for x in self.elements)}]'

class BaseFunction(Value):
	def __init__(self, name):
		super().__init__()
		self.name = name or "<anonymous>"

	def generate_new_context(self):
		new_context = Context(self.name, self.context, self.pos_start)
		new_context.symbol_table = SymbolTable(new_context.parent.symbol_table)
		return new_context
	
	def check_args(self, arg_names, args):
		res = RTResult()

		if len(args) > len(arg_names):
				return res.failure(RTError(
					self.pos_start, self.pos_end,
					f"{len(args) - len(arg_names)} Te pasaste de rosca con los Jugadores '{self.name}'",
					self.context
				))
			
		if len(args) < len(arg_names):
			return res.failure(RTError(
				self.pos_start, self.pos_end,
				f"{len(arg_names) - len(args)} No le pasaste todos los Jugadores '{self.name}'",
				self.context
			))	
		
		return res.success(None)

	def populate_args(self, arg_names, args, exec_ctx):
		for i in range(len(args)):
			arg_name = arg_names[i]
			arg_value = args[i]
			arg_value.set_context(exec_ctx)
			exec_ctx.symbol_table.set(arg_name, arg_value)

	def check_and_populate_args(self, arg_names, args, exec_ctx):
		res = RTResult()
		res.register(self.check_args(arg_names, args))
		if res.should_return() : return res
		self.populate_args(arg_names, args, exec_ctx)
		return res.success(None)

class Function(BaseFunction):
	def __init__(self, name, body_node, arg_names, should_auto_return):
		super().__init__(name)
		self.body_node = body_node
		self.arg_names = arg_names
		self.should_auto_return = should_auto_return

	def execute(self, args):
		from fulvo.interpreter import Interpreter

		res = RTResult()
		interpreter = Interpreter()
		exec_ctx = self.generate_new_context()

		res.register(self.check_and_populate_args(self.arg_names, args, exec_ctx))
		if res.should_return(): return res

		value = res.register(interpreter.visit(self.body_node, exec_ctx))
		if res.should_return() and res.func_return_value == None: return res

		ret_value = (value if self.should_auto_return else None) or res.func_return_value or Number.null
		return res.success(ret_value)

	def copy(self):
		copy = Function(self.name, self.body_node, self.arg_names, self.should_auto_return)
		copy.set_context(self.context)
		copy.set_pos(self.pos_start, self.pos_end)
		return copy

	def __repr__(self):
		return f"<function {self.name}>"

class BuiltInFunction(BaseFunction):
	def __init__(self, name):
		super().__init__(name)

	def execute(self, args):
		res = RTResult()
		exec_ctx = self.generate_new_context()
	
		method_name = f'execute_{self.name}'
		method = getattr(self, method_name, self.no_visit_method)
		
		res.register(self.check_and_populate_args(method.arg_names, args, exec_ctx))
		if res.should_return(): return res

		return_value = res.register(method(exec_ctx))
		if res.should_return(): return res

		return res.success(return_value)

	def no_visit_method(self, args, exec_ctx):
		raise Exception(f'No visit_{self.name} method defined')

	def copy(self):
		copy = BuiltInFunction(self.name)
		copy.set_context(self.context)
		copy.set_pos(self.pos_start, self.pos_end)
		return copy
	
	def __repr__ (self):
		return f'<built-in function {self.name}>'

	#################################################
	# BUILT-IN FUNCTIONS
	#################################################

	def execute_print(self, exec_ctx):
		print(str(exec_ctx.symbol_table.get("value")))
		return RTResult().success(Number.null)
	execute_print.arg_names = ["value"]

	def execute_print_ret(self, exec_ctx):
		return RTResult().success(String(str(exec_ctx.symbol_table.get("value"))))
	execute_print_ret.arg_names = ["value"]

	def execute_input(self, exec_ctx):
		text = input()
		return RTResult().success(String(text))
	execute_input.arg_names = []
	
	def execute_input_int(self, exec_ctx):
		while True:
			text = input()
			try:
				number = int(text)
				break
			except ValueError:
				print(f"'{text}' is not an integer. Try again.")

		return RTResult().success(Number(number))
	execute_input_int.arg_names = []

	def execute_clear(self, exec_ctx):
		os.system('cls' if os.name == 'nt' else 'clear')
		return RTResult().success(Number.null)
	execute_clear.arg_names = []

	def execute_is_number(self, exec_ctx):
		is_number = isinstance(exec_ctx.symbol_table.get("value"), Number)
		return RTResult().success(Number.true if is_number else Number.false)
	execute_is_number.arg_names = ["value"]

	def execute_is_string(self, exec_ctx):
		is_string = isinstance(exec_ctx.symbol_table.get("value"), String)
		return RTResult().success(Number.true if is_string else Number.false)
	execute_is_string.arg_names = ["value"]

	def execute_is_list(self, exec_ctx):
		is_list = isinstance(exec_ctx.symbol_table.get("value"), List)
		return RTResult().success(Number.true if is_list else Number.false)
	execute_is_list.arg_names = ["value"]
		
	def execute_is_function(self, exec_ctx):
		is_function = isinstance(exec_ctx.symbol_table.get("value"), BaseFunction)
		return RTResult().success(Number.true if is_function else Number.false)
	execute_is_function.arg_names = ["value"]
	
	def execute_append(self, exec_ctx):
		list_ = exec_ctx.symbol_table.get("list")
		value = exec_ctx.symbol_table.get("value")

		if not isinstance(list_, List):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"First argument must be list",
				self.context
			))
		
		list_.elements.append(value)
		return RTResult().success(Number.null)
	execute_append.arg_names = ["list", "value"]

	def execute_pop(self, exec_ctx):
		list_ = exec_ctx.symbol_table.get("list")
		index = exec_ctx.symbol_table.get("index")

		if not isinstance(list_, List):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"First argument must be list",
				self.context
			))
		if not isinstance(index, Number):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"Second argument must be number",
				self.context
			))

		try:
			element = list_.elements.pop(index.value)
		except:
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				'Element at this index could not be removed from list',
				self.context
			))
		
		return RTResult().success(element)
	execute_pop.arg_names = ["list", "index"]

	def execute_extend(self, exec_ctx):
		listA = exec_ctx.symbol_table.get('listA')
		listB = exec_ctx.symbol_table.get('listB')

		if not isinstance(listA, List):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"First argument must be list",
				self.context
			))
		
		if not isinstance(listB, List):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				'Second argument must be list',
				self.context
			))
		
		listA.elements.extend(listB.elements)
		return RTResult().success(Number.null)
	execute_extend.arg_names = ['listA', 'listB']

	def execute_len(self, exec_ctx):
		list_ = exec_ctx.symbol_table.get("list")

		if not isinstance(list_, List):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"Argument must be list",
				exec_ctx))
		
		return RTResult().success(Number(len(list_.elements)))
	execute_len.arg_names = ["list"]

	def execute_run(self, exec_ctx):
		fn = exec_ctx.symbol_table.get("fn")

		if not isinstance(fn, String):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"First argument must be string",
				exec_ctx
			))

		fn = fn.value

		try:
			with open(fn,"r") as f:
				script = f.read()
		except Exception as e:
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				f"Failed to load script \"{fn}\"",
				exec_ctx
			))
		
		_ , error = run(fn, script)
		if error:
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				f"Failed to finish executing script \"{fn}\"" + error.as_string(),
				exec_ctx
			))
		
		return RTResult().success(Number.null)
	execute_run.arg_names = ['fn']

	def execute_historico(self, exec_ctx):
		dios()
		return RTResult().success(Number.null)
	execute_historico.arg_names = []

	def execute_tiempo(self, exec_ctx):
		sleep_time = exec_ctx.symbol_table.get("value")
		if isinstance(sleep_time, Number):
			sleep(sleep_time.value)
			return RTResult().success(Number.null)
		else :
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"No podemos hacer tiempo si no pones por cuantos segundo queres hacerlo",
				exec_ctx
			))
		return RTResult().success(Number.null)
	execute_tiempo.arg_names = ['value']

	def execute_lesionar(self, exec_ctx):
		var = exec_ctx.symbol_table.get('var')
		if isinstance(var, Number):
			print(f"{var} se ha lesionado, fractura de perone")
			del var #Intento eliminar la variable jaja no se como hacerlo todavia
		else:
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"UFF se salvo, no lo lesionaste de pedo",
				exec_ctx
			))

		return RTResult().success(Number.null)
	execute_lesionar.arg_names = ['var']

	def execute_cabezaso(self, exec_ctx):
		print("\nComo le vas a dar un cabezaso a Materazzi?")
		sleep(1)
		print("\nTe vas a tener que ir pelado")
		sleep(2)
		print("\n \033[91m *Saca roja* \033[0m")
		sleep(2)
		sys.exit(0)
		return RTResult().success(Number.null) # never reached
	execute_cabezaso.arg_names = []

	def execute_ankara(self, exec_ctx):
		print ("Inmeso Messi")
		sleep(1)
		print ("Ankara Messi, Ankara Messi, Ankara")
		sleep(1)
		print ("Gollll")
		return RTResult().success(Number.null)
	execute_ankara.arg_names = []

	def execute_bicho(self,exec_ctx):
		print("SIUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU")
		return RTResult().success(Number.null)
	execute_bicho.arg_names = []

	def execute_boca(self, exec_ctx):
		var = exec_ctx.symbol_table.get('var')
		
		print("El santo consejo del futbol esta analizando su peticion...")
		sleep(3)
		if isinstance(var, Number):
			var.value = "12" #Intento cambiar el valor de la variable jaja no se como hacerlo todavia
		elif isinstance(var, String):
			var.value = "BOCAAA"
		else:
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"Tu jugador no es apto para ser de Boca.", 
				exec_ctx
			))
		return RTResult().success(var)
	execute_boca.arg_names = ['var']

	def execute_esBoca(self,exec_ctx):
		var = exec_ctx.symbol_table.get('var')
		print("Disculpe, esto es Boca?")
		if isinstance(var, String):
			if var.value in ("BOCA", "Maradona", "Riquelme", "Palermo", "Tevez"):
				print("Si, esto es BOCAAAAAAAAAAAA")
				return RTResult().success(Number.true)
			else:
				if var.value not in ("River", "Quintero", "Martinez", "Burrito", "Alvarez", "Gas pimienta"):
					print("No jefe, esto no es Boca")
				else:
					print("Tenes menos de 10 segundos para irte y que no te agarremos con la 12")
				return RTResult().success(Number.false)
		else:
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"No podes preguntarme si este mamarracho es Boca.", 
				exec_ctx
			))
	execute_esBoca.arg_names = ['var']

	def execute_river(self, exec_ctx):
		### No se me ocurre nada
		print ("Hacela personal y ahi se va")
		sleep(1)
		print ("Se va se va")
		sleep(1)
		print ("Se viene Martinez para el gol")
		sleep(1)
		print ("Y va el tercero")
		sleep(0.4)
		print ("Y va el tercero")
		sleep(0.4)
		print ("Y va el tercero")
		sleep(0.4)
		print ("Y gol de \033[31mRiver \033[0m")
		sleep(0.4)
		print ("Y gol de \033[31mRiverrrrrrrrrrrrrrrrr \033[0m")
		sleep(1)
		print ("GOLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
		sleep(4)
		print ("Moriste en \033[31m madrid \033[0m bostero")
		return RTResult().success(Number.null)
	execute_river.arg_names = []