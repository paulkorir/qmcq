# QMCQ - Quick MCQ Quiz

A simple MCQ (Multiple Choice Questions) quiz application powered by Python.

## Overview

`qmcq` provides an interactive command-line interface to participate in multiple-choice quizzes. You supply a JSON file containing questions, options, and answers, and `qmcq` guides you through the quiz, shuffling questions and options for a unique experience every time.

## Features

- **Randomization**: Both questions and answer choices are shuffled to ensure a unique quiz-taking experience every time.
- **JSON Powered**: Easy to supply quizzes in a readable and structured JSON format.
- **Validation**: The application validates the structure of the JSON against a predefined schema to ensure quiz integrity.

## Installation

To install `qmcq`, you can use `pip`:

```bash
pip install qmcq
```

## Usage

After installation, you can run the quiz using:

```bash
qmcq path_to_your_quiz.json
```

Replace `path_to_your_quiz.json` with the path to your quiz file.

## JSON Structure

A sample structure for the quiz JSON file:

```json
{
  "questions": [
    {
      "question": "What is the capital of France?",
      "options": ["Berlin", "Madrid", "Rome", "Paris"],
      "answer": "Paris"
    },
    {
      "question": "Which is the largest mammal?",
      "options": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
      "answer": "Blue Whale"
    }
    // ... add more questions as needed
  ]
}
```

## Contributing

We welcome contributions! Please fork the repository and open a pull request with your changes.

## License

This project is licensed under the Apache-2.0 License.

