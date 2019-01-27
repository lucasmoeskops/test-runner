import json
from os.path import dirname, join

from program import Program


def read_program_manifest(program_module) -> Program:
    module = __import__(program_module).main

    try:
        manifest = open(
            join(dirname(module.__file__), 'test-runner.manifest'), 'r')
    except TypeError as e:
        raise ValueError('Program doesn\'t define a manifest file')

    data = json.load(manifest)
    return Program(
        name=data.get('name', '?'),
        main=getattr(module, data['main']),
        expected_output=data.get('expected_result')
    )
