"""
automation_controller.py

Coordinates all automation components.
"""

from leetcode_automation.services.automation_workflow import (
    AutomationWorkflow,
)


class AutomationController:
    """Coordinates the automation workflow."""

    def __init__(self) -> None:
        """Initialize the automation controller."""

        self._workflow = AutomationWorkflow()

    def process_solution(self, path: str) -> None:
        """Process a newly detected solution."""

        self._workflow.run(path)