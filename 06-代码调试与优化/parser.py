#!/usr/bin/env python
# encoding: utf-8

from configparser import ConfigParser
import yaml

cfg = ConfigParser()
cfg.read('config.ini')
print(cfg.sections())
print(cfg.get('Common', 'version'))

f = open('config.yaml')
content = yaml.load(f)
print(content)
