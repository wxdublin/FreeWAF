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

# create a generator to get each yaml file content in a given path
def get_yaml_rules(path=None):
    from fnmatch import fnmatch
    if path == None:
        path = os.getcwd()
    for file in os.listdir(path):
        if fnmatch(file, '*.yaml'):
            with open(file, 'r') as fd:
                yield {file: fd.read()}

def load_yaml_rules(yaml_rules):
    try:
        rules_iter = yaml.load_all(yaml_rules)
    except yaml.YAMLError, e:
        if hasattr(e, 'problem_mark'):
            mark = e.problem_mark
            print "Error position: (%s:%s)" % (mark.line+1, mark.column+1)
        rules_iter = None
    return rules_iter

def generate_lua_rules(rules_iter, version="0.5", comments=None):
    lua_tpl = """
    -- {{ comments }}
    local _M = {}

    _M.version = {{ version }}

    local _rules = {
    {{ _lua_rules }}
    }

    funcation _M.rules()
        return _rules
    end

    return _M
    """
    if not rules_dict:
        return

    for rule  in rules_iter:
        _rule = #FIXME
