from results import Results
from termcolor import colored
from utils import humanize_number


class Report:
    def __init__(self, results: Results):
        self.results = results

    def write(self, fp):
        fp.write(self.format_headline('Test-runner report:\n\n'))

        for result in self.results:
            fp.write(self.format_headline('Program execution result:\n'))
            fp.write(
                self.format_text('Name: {}\n'.format(result.program.name)))

            if result.execution_time < 0.1:
                time_format = self.format_excellent
            elif result.execution_time < 1.0:
                time_format = self.format_success
            elif result.execution_time < 10.0:
                time_format = self.format_text
            elif result.execution_time < 60:
                time_format = self.format_warning
            else:
                time_format = self.format_error
            fp.write(
                self.format_text(
                    'Execution time: {}\n'.format(
                        time_format(humanize_number(result.execution_time)))))

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
