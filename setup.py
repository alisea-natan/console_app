from setuptools import setup


def read_requirements():
    with open("requirements.txt", "r") as file:
        requirements = [line.rstrip('\n') for line in file]
    return requirements


setup(
    name='console_app',
    version='0.1.0',
    description='This program is simple check how to create and use setup.py, click, poetry in project',
    author='alisea-natan',
    email='liskin.sun@gmail.com',
    python_requires='>=3.8.0',
    packages=['hello', 'config'],
    package_data={
        'config': ['*'],
        'hello': ['*']
    },
    install_requires=read_requirements(),
    entry_points={
        'console_scripts': [
            'greeting = hello.main:hi'
        ]

    }
)
