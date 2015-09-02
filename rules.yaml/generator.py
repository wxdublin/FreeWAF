#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import yaml
from jinja2 import Environment, FileSystemLoader


file = open('10000.yaml', 'r')

ct = file.read()
print(ct)

rules = yaml.load_all(ct)

rules = list(rules)
print(rules)
env = Environment(loader=FileSystemLoader(os.getcwd()))
tpl = env.get_template('template.jinja2')
print(tpl.render(rules=rules))
