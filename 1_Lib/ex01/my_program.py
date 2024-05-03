import sys
sys.path.append('./local_lib')

from path import Path

# Create a directory and a file within it
dir_path = Path('example_directory')
dir_path.mkdir_p()

file_path = dir_path / 'example_file.txt'
file_path.write_text('Hello from path.py!')

# Read the file and display its contents
content = file_path.read_text()
print(content)

