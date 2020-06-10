from setuptools import setup

setup(
    name='quantconnect-lean-stubs',
    version='0.1.0',
    author='QuantConnect Corp.',
    author_email='support@quantconnect.com',
    packages=[
        'QuantConnect',
        'QuantConnect.Data',
        'QuantConnect.Securities',
        'QuantConnect.Algorithm',
    ],
    package_data={
        'QuantConnect': ['py.typed', '*.pyi'],
        'QuantConnect.Data': ['py.typed', '*.pyi'],
        'QuantConnect.Securities': ['py.typed', '*.pyi'],
        'QuantConnect.Algorithm': ['py.typed', '*.pyi'],
    },
    url='https://www.quantconnect.com',
    license='LICENSE.md',
    description='Python type definitions for the Lean algorithmic trading engine',
    python_requires='>=3.6'
)

