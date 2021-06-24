from setuptools import setup, find_packages

setup(
    name='console_app',
    version='0.1.0',
    description='This program is simple check how to create and use setup.py in project',
    author="alisea-natan",
    packages=['hello', 'config'],
    package_data={
        'config': ['*'],
        'hello': ['*']
    },
    install_requires=['pyyaml', 'click'],
    entry_points={
        'console_scripts': [
            'greeting = hello.main:hi'
        ]

    }
)
