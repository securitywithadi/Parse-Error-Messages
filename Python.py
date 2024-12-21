import re
from collections import defaultdict

def parse_log_file(file_path):
    """
    Parses a log file for error messages and groups them by error type.

    Args:
        file_path (str): Path to the log file.

    Returns:
        dict: A dictionary with error types as keys and lists of messages as values.
    """
    error_dict = defaultdict(list)
    
    # Regular expression to capture error type and message (customize based on log format)
    error_pattern = re.compile(r"ERROR\s+(\w+):\s+(.*)")

    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            for line in file:
                match = error_pattern.search(line)
                if match:
                    error_type = match.group(1)  # Captures the error type
                    error_message = match.group(2)  # Captures the error message
                    error_dict[error_type].append(error_message)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return dict(error_dict)

# Example usage
file_path = 'logfile.txt'  # Replace with the path to your log file
error_messages = parse_log_file(file_path)
for error_type, messages in error_messages.items():
    print(f"Error Type: {error_type}")
    for msg in messages:
        print(f"  - {msg}")
