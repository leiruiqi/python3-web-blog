#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Configuration
'''

__author__ = 'Michael Liao'

import config_default,os

class Category():
    def __init__(self,id,name):
        self.id = id
        self.name = name

categorys = [Category('1','日志'),Category('2','编程')]

class Dict(dict):
    '''
    Simple dict but support access as x.y style.
    '''
    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

def merge(defaults, override):
    r = {}
    for k, v in defaults.items():
        if k in override:
            if isinstance(v, dict):
                r[k] = merge(v, override[k])
            else:
                r[k] = override[k]
        else:
            r[k] = v
    return r

def toDict(d):
    D = Dict()
    for k, v in d.items():
        D[k] = toDict(v) if isinstance(v, dict) else v
    return D

configs = config_default.configs


import sys,getopt
env='dev'
opts, args = getopt.getopt(sys.argv[1:],'', ['env='])
for op, value in opts:
    if (op == '--env'):
        print('env',value)
        env = value


print('env=',env)
try:

    if env == 'pro':
        import config_override
        configs = merge(configs, config_override.configs)
except ImportError:
    pass

configs = toDict(configs)
