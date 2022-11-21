import os


if __name__ == '__main__':
    os.system('pip freeze > requirements_pip.txt')
    os.system('conda list -e > requirements_conda.txt')