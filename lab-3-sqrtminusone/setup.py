from setuptools import setup, find_packages

setup(
    name='lab3_example',
    version='0.0.1',
    description='TODO',
    author='SqrtMinusOne',
    author_email='thexcloud@gmail.com',
    packages=find_packages(),
    install_requires=['click', 'sqlalchemy', 'mysql-connector-python', 'dotenv'],
    entry_points='''
    [console_scripts]
    lab3_example=lab3_example.cli:cli
    '''
)
