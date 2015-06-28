from setuptools import setup

install_requires = [
    'requests',
    'beautifulsoup4'
]

setup(
    name='urbandefinition',
    install_requires=install_requires,
    version=0.3,
    description='Get Urban Dictionary definitions from the terminal',
    author='Asad Dhamani',
    author_email='dhamaniasad+code@gmail.com',
    url='https://github.com/dhamaniasad/urbandefinition',
    license='Unlicense',
    py_modules=['urbandefinition'],
    entry_points={
        'console_scripts': [
            'urban = urbandefinition:command_line_runner'
        ]
    }
)