def foo(a, b = 10, *c, d,**kw):
    pass

import inspect
import sys,getopt,os

sig = inspect.signature(foo)
sig.parameters
sig.parameters.items()
sig.parameters.values()
sig.parameters.keys()
for name, param in sig.parameters.items():
    print(name+' type=',param.kind)


opts, args = getopt.getopt(sys.argv[1:],'', ['env='])
for op, value in opts:

    if (op == '--env'):
        print('value='+value)
        os.putenv('env', value)

env = os.getenv('env')

os.putenv('abc','a')
os.p
a=os.getenv('abc')
print('env=',env)
print('a=',a)
from config import configs
print(configs)