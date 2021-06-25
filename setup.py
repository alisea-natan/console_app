from setuptools import setup

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
    install_requires=['pyyaml >= 5.4.1', 'click >= 8.0.1'],
    entry_points={
        'console_scripts': [
            'greeting = hello.main:hi'
        ]

    }
)
