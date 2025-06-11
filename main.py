import argparse
import json
import yaml
import xml.etree.ElementTree as ET

def parse_arguments():
    parser = argparse.ArgumentParser(description="Data conversion software")
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("output_file", help="Path to the output file")
    return parser.parse_args()

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError as e:
        print(f"Error- JSON: {e}")
        return None
    
def save_json(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error- save to JSON: {e}")

def load_xml(file_path):
    try:
        tree = ET.parse(file_path)
        return tree.getroot()
    except ET.ParseError as e:
        print(f"Error- XML: {e}")
        return None

def save_yaml(file_path, data):
    try:
        with open(file_path, 'w') as file:
            yaml.dump(data, file, default_flow_style=False)
    except Exception as e:
        print(f"Error- save to YAML: {e}")

def load_xml(file_path):
    try:
        tree = ET.parse(file_path)
        return tree.getroot()
    except ET.ParseError as e:
        print(f"Error- XML: {e}")
        return None

def save_xml(file_path, root):
    try:
        tree = ET.ElementTree(root)
        tree.write(file_path)
    except Exception as e:
        print(f"Error- save to XML: {e}")
