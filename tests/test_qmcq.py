import json
import unittest
from unittest.mock import patch

from qmcq.quiz import quiz, validate_data
from qmcq.schema import schema


class TestQMCQ(unittest.TestCase):

    def setUp(self):
        self.sample_data = json.dumps({
            "questions": [
                {
                    "question": "What is the capital of France?",
                    "options": ["Berlin", "Madrid", "Rome", "Paris"],
                    "answer": "Paris"
                }
            ]
        })

    def test_validate_data_valid(self):
        result = validate_data(self.sample_data, schema)
        self.assertTrue(result)

    def test_validate_data_invalid(self):
        invalid_data = json.dumps({
            "questions": [
                {
                    "question": "What is the capital of France?",
                    "options": ["Berlin", "Madrid", "Rome"],
                    "answer": "Paris"
                }
            ]
        })
        result = validate_data(invalid_data, schema)
        self.assertFalse(result)

    @patch("builtins.input", return_value="A")
    @patch("builtins.print")
    def test_quiz(self, mock_print, mock_input):
        quiz(self.sample_data, shuffle=False)
        mock_print.assert_any_call("Correct!\n")

    @patch("builtins.input", return_value="B")
    @patch("builtins.print")
    def test_quiz_wrong_answer(self, mock_print, mock_input):
        quiz(self.sample_data)
        mock_print.assert_any_call("Wrong! The correct answer is: Paris\n")


if __name__ == "__main__":
    unittest.main()
