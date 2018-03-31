def foo(a, b = 10, *c, d,**kw):
    pass

import inspect

sig = inspect.signature(foo)
sig.parameters
sig.parameters.items()
sig.parameters.values()
sig.parameters.keys()
for name, param in sig.parameters.items():
    print(name+' type=',param.kind)


from config import configs
print(configs)