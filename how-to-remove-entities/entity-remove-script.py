
from rasa.nlu.training_data import load_data
import argparse

arg_parser = argparse.ArgumentParser(description="Replace entity labels in a story file.")
arg_parser.add_argument("input", help="Name of the input file")
arg_parser.add_argument("output", help="Name of the output file")

if __name__ == '__main__':

    args = arg_parser.parse_args()

    data = load_data(args.input)

    for e in data.training_examples:
    	e.set("entities", [])

    with open(args.output, "w+") as f:
    	f.write(data.nlu_as_markdown())

