from setuptools import setup, find_packages

setup(
    name="deep_learning_edu",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'PyQt6>=6.5.0',
        'torch>=2.0.0',
        'torchvision>=0.15.0',
        'numpy>=1.24.0',
        'pandas>=2.0.0',
        'transformers>=4.30.0',
        'sqlalchemy>=2.0.0',
        'pillow>=10.0.0'
    ]
)