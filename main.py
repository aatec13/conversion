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
        
def convert(input_file, output_file):
    input_extension = input_file.split('.')[-1]
    output_extension = output_file.split('.')[-1]

    if input_extension == "json":
        data = load_json(input_file)
    elif input_extension in ["yml", "yaml"]:
        data = load_yaml(input_file)
    elif input_extension == "xml":
        data = load_xml(input_file)
    else:
        print("Unsupported input format")
        return
    
    if data is None:
        print("Error reading the input file")
        return
    
    if output_extension == "json":
        save_json(output_file, data)
    elif output_extension in ["yml", "yaml"]:
        save_yaml(output_file, data)
    elif output_extension == "xml":
        save_xml(output_file, data)
    else:
        print("Unsupported output format")

def main():
    args = parse_arguments()
    convert(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
