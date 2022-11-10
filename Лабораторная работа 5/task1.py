# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint

pprint([{'bin': bin(deci), 'dec': deci, 'hex': hex(deci), 'oct': oct(deci)} for deci in range(16)])
