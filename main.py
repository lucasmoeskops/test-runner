import json
import sys
from sys import stdout
from typing import Any

from parsing import read_program_manifest
from reports import TerminalReport
from runner import Runner


def execute_manifest(fp):
    def try_read_program_manifest(module) -> Any:
        try:
            return read_program_manifest(module)
        except ValueError as e:
            print(e)
            return None

    manifest = json.load(fp)
    programs = filter(
        None, map(try_read_program_manifest, manifest['programs']))
    runner = Runner(programs)
    report = TerminalReport(runner.run())
    report.write(stdout)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        manifest_name = sys.argv.pop()
    else:
        manifest_name = 'test-runner.manifest'

    if len(sys.argv) == 1:
        # Read manifest file and execute modules in manifest
        sys.path.append('')
        source = open(manifest_name, 'r')
        execute_manifest(source)
