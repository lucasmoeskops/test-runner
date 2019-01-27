from typing import Any, Callable, Dict, Optional


class Program:
    def __init__(self, name: str, main: Callable, expected_output: Any, execute_kwargs: Optional[Dict]=None):
        self.name: str = name
        self.main: Callable = main
        self.expected_output: Any = expected_output
        self.execute_kwargs: Dict = execute_kwargs or {}

    def execute(self, **kwargs) -> Any:
        return self.main(**kwargs)
