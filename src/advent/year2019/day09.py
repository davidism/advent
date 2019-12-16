from advent.year2019.intcode import Interpreter
from advent.year2019.intcode import read_intcode

data = read_intcode()
c = Interpreter(data, [1])
c.run()
print(c.output[0])
c = Interpreter(data, [2])
c.run()
print(c.output[0])
