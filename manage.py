#!/usr/bin/env python

from todo         import todo
from flask_script import Manager, Server

mgr = Manager(todo)
mgr.add_command('runserver', Server(host = '0.0.0.0', port = 8080))

@mgr.command
def functests():
    '''Run functional tests'''
    from unittest import TestLoader, TextTestRunner
    tests = TestLoader().discover('.', pattern = 'functional_tests.py')
    TextTestRunner(verbosity = 2).run(tests)

@mgr.command
def unittests():
    '''Run unit tests'''
    from unittest import TestLoader, TextTestRunner
    tests = TestLoader().discover('.', pattern = 'unit_tests.py')
    TextTestRunner(verbosity = 2).run(tests)


if __name__ == '__main__':
    mgr.run()
