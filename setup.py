import subprocess

requirement_path = 'requirement.txt'

venv_activation='myenv\\Scripts\\activate'


requirements = []
with open(requirement_path, 'r') as file:
    requirements = [line.strip() for line in file]

for package in requirements:
    install_command = f'pip install {package}'
    full_command = f'{venv_activation} && {install_command}'
    subprocess.run(full_command, shell=True, text=True, capture_output=True)
    print(install_command,"-----> Done")
