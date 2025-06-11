import argparse
import json
import yaml
import xml.etree.ElementTree as ET

def parse_arguments():
    parser = argparse.ArgumentParser(description="Data conversion software")
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("output_file", help="Path to the output file")
    return parser.parse_args()
