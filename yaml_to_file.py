import argparse
import base64
import os
import yaml

def base64_decode_and_write(filename):
    with open(filename, 'r') as file:
        # Load YAML file
        file_content = yaml.safe_load(file)

    # Extract base64 string
    base64_str = file_content.get('options', {}).get('value', '').replace('\n', '')

    # Base64 decode
    decoded_str = base64.b64decode(base64_str)

    # Output file name from YAML file
    output_filename = file_content.get('output', {}).get('filename', '')

    # Output directory same as input directory
    output_dir = os.path.dirname(os.path.abspath(filename))

    # Write the decoded content to the file
    with open(os.path.join(output_dir, output_filename), 'wb') as file:
        file.write(decoded_str)

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', metavar='N', type=str, nargs='+',
                        help='input files to process')
    args = parser.parse_args()

    # Process each file
    for filename in args.filenames:
        base64_decode_and_write(filename)
