#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import yaml
from jinja2 import Environment, FileSystemLoader
from fnmatch import fnmatch


file = open('10000.yaml', 'r')

ct = file.read()
print(ct)

rules = yaml.load_all(ct)

rules = list(rules)
print(rules)
env = Environment(loader=FileSystemLoader(os.getcwd()))
tpl = env.get_template('template.jinja2')
print(tpl.render(rules=rules))

class YtL(object):

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

    _yaml_text = '';
    _yaml_rules = '';
    _rules_data = '';
    _lua_rules = '';

    def __init__(self, path=None, **kwargs):
        if not path:
            path = os.getcwd()
        self.options = kwargs,

    # create a generator to get each yaml file content in a given path
    def _get_yaml_rules(self):
        for file in os.listdir(self.path):
            if fnmatch(file, '*.yaml'):
                with open(file, 'r') as fd:
                    yield {file: fd.read()}

    def _load_yaml_rules(self):
        try:
            rules_iter = yaml.load_all(self._yaml_rules)
        except yaml.YAMLError, e:
            if hasattr(e, 'problem_mark'):
                mark = e.problem_mark
                print "Error position: (%s:%s)" % (mark.line+1, mark.column+1)
            rules_iter = None
        return rules_iter

    def generate_lua_rules(self, rules_iter, version="0.5", comments=None):
       if not rules_iter:
            return

       for rule  in rules_iter:
            _rule = None #FIXME


class Render(object):
    def __init__(self, **kwargs):
        # TODO
        self.options = kwargs

    def num(self, k, v):
        return "'%s': %d" % (k, v)

    def dict(self, k, v):
        return
