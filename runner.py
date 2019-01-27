from time import time

from aspects import Aspect
from program import Program
from typing import Iterable, List, Optional

from results import Results, Result


class Runner:
    def __init__(self,
                 programs: Iterable[Program],
                 aspects: Optional[Iterable[Aspect]]=None):
        self.aspects: List[Aspect] = list(aspects or ())
        self.programs: List[Program] = list(programs)

    def run(self) -> Results:
        results = Results()

        for program in self.programs:
            results.add_result(self.test_program(program))

        return results

    def test_program(self, program: Program) -> Result:
        for aspect in self.aspects:
            aspect.prepare(program)

        before = time()
        return_value = program.execute()
        after = time()

        result = Result(program, return_value, after - before)

        for aspect in self.aspects:
            aspect.examine(result)

        return result
