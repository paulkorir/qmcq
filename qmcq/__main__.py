import argparse
import sys

from .quiz import quiz, validate_data, load_json_from_file


def main():
    parser = argparse.ArgumentParser(description="Run the MCQ Quiz from a JSON file.")
    parser.add_argument("json_file", type=str, help="The name of the JSON file containing quiz data.")
    parser.add_argument("--schema", default="qmcq.jsonschema", type=str, help="The name of the JSON schema file.")
    args = parser.parse_args()

    schema = load_json_from_file(args.schema)

    data = load_json_from_file(args.json_file)

    if validate_data(data, schema):
        quiz(data)
        return 0
    else:
        print("The data did not pass the schema validation!")
        return 1


if __name__ == "__main__":
    sys.exit(main())
