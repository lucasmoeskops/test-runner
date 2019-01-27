from program import Program
from results import Result


class Aspect:
    def prepare(self, program: Program):
        raise NotImplementedError()

    def examine(self, result: Result):
        raise NotImplementedError()


class AverageRunningTime(Aspect):
    def prepare(self, program: Program):
        pass

    def examine(self, result):
        pass
