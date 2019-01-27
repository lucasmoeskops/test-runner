from operator import attrgetter
from typing import Any, List

from program import Program


class Result:
    def __init__(self,
                 program: Program,
                 return_value: Any,
                 execution_time: float=None):
        self.program: Program = program
        self.execution_time: float = execution_time
        self.return_value: Any = return_value
        self.expected_result: bool = return_value == program.expected_output


class Results:
    def __init__(self):
        self.program_results: List[Result] = []

    def __iter__(self):
        return iter(self.program_results)

    @property
    def total_execution_time(self):
        return sum(map(attrgetter('execution_time'), self.program_results))

    @property
    def average_execution_time(self):
        return self.total_execution_time / len(self.program_results)

    def add_result(self, result: Result):
        self.program_results.append(result)
