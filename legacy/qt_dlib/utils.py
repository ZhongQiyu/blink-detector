import json

def load_configuration(file_path):
    """Load configuration settings from a JSON file."""
    try:
        with open(file_path, 'r') as config_file:
            config = json.load(config_file)
        return config
    except FileNotFoundError:
        print(f"The configuration file {file_path} was not found.")
        exit(1)
    except json.JSONDecodeError:
        print(f"The configuration file {file_path} is not valid JSON.")
        exit(1)
