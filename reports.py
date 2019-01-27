from results import Results
from termcolor import colored
from utils import humanize_time


class Report:
    def __init__(self, results: Results):
        self.results = results

    def write(self, fp):
        fp.write(self.format_headline('Test-runner report:\n\n'))

        for result in self.results:
            fp.write(self.format_headline('Program execution result:\n'))
            fp.write(
                self.format_text('Name: {}\n'.format(result.program.name)))

            time_format = self._time_format(result.execution_time)
            fp.write(
                self.format_text(
                    'Execution time: {}\n'.format(
                        time_format(humanize_time(result.execution_time)))))

            if result.expected_result:
                fp.write(
                    self.format_success(
                        'Return value: {} (expected)\n'.format(
                            result.return_value)))
            else:
                fp.write(
                    self.format_warning(
                        'WARNING: invalid return value: '
                        '{} (expected {})\n'.format(
                            result.return_value,
                            result.program.expected_output)))

            fp.write('\n')

        fp.write(
            self.format_text(
                'Total execution time: {}\n'.format(
                    humanize_time(self.results.total_execution_time))))
        avg_time = self.results.average_execution_time
        time_format = self._time_format(avg_time)
        fp.write(
            self.format_text(
                'Average program execution time: {}\n'.format(
                    time_format(humanize_time(avg_time)))))
        fp.write(self.format_headline('End of report\n'))

    def format_headline(self, headline: str) -> str:
        return headline

    def format_text(self, text: str) -> str:
        return text

    def format_warning(self, warning: str) -> str:
        return warning

    def format_success(self, success: str) -> str:
        return success

    def format_error(self, error: str) -> str:
        return error

    def format_excellent(self, text: str) -> str:
        return text + '!'

    def _time_format(self, time: float):
        if time < 0.1:
            return self.format_excellent
        if time < 1.0:
            return self.format_success
        if time < 10.0:
            return self.format_text
        if time < 60:
            return self.format_warning
        else:
            return self.format_error


class TerminalReport(Report):
    def format_headline(self, headline: str) -> str:
        return colored(headline, 'blue', attrs=['bold'])

    def format_text(self, text: str) -> str:
        return colored(text, 'white')

    def format_warning(self, warning: str) -> str:
        return colored(warning, 'yellow')

    def format_success(self, success: str) -> str:
        return colored(success, 'green')

    def format_error(self, error: str) -> str:
        return colored(error, 'red')

    def format_excellent(self, error: str) -> str:
        return colored(error, 'magenta', attrs=['bold'])
