#!/usr/bin/env python
# encoding: utf-8

from configparser import ConfigParser
import yaml

cfg = ConfigParser()
cfg.read('config.ini')
print(cfg.sections())    # ['Chrome', 'IE', 'Common', 'SmartRepair']
print(cfg.get('Common', 'version'))    # 2.0.0.88

f = open('config.yaml')
content = yaml.load(f)
print(content)    # {'name': 'junxi', 'age': 18, 'spouse': {'name': 'Rui', 'age': 18}, 
                  #  'children': [{'name': 'Chen You', 'age': 3}, {'name': 'Ruo Xi', 'age': 2}]}
