import unittest
from src.tasks.automation import TaskAutomation
from src.tasks.executor import TaskExecutor

class TestTaskAutomation(unittest.TestCase):

    def setUp(self):
        self.task_automation = TaskAutomation()
        self.task_executor = TaskExecutor()

    def test_automate_task_valid_intent(self):
        intent = "turn on the lights"
        result = self.task_automation.automate_task(intent)
        self.assertTrue(result)

    def test_automate_task_invalid_intent(self):
        intent = "unknown command"
        result = self.task_automation.automate_task(intent)
        self.assertFalse(result)

class TestTaskExecutor(unittest.TestCase):

    def setUp(self):
        self.task_executor = TaskExecutor()

    def test_execute_command_valid_command(self):
        command = "play music"
        result = self.task_executor.execute_command(command)
        self.assertTrue(result)

    def test_execute_command_invalid_command(self):
        command = "invalid command"
        result = self.task_executor.execute_command(command)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()