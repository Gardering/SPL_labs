import os

def save_to_file(filename, content):
    output_path = os.path.join('config', filename)
    os.makedirs('config', exist_ok=True)
    with open(output_path, 'w') as file:
        file.write(content)
