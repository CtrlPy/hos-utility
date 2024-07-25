from setuptools import setup, find_packages
import pathlib

HERE = pathlib.Path(__file__).parent

long_description = (HERE / "README.md").read_text()

setup(
    name="hos-utility",
    version="1.0.3",
    packages=find_packages(),
    install_requires=[
        "urwid",
    ],
    entry_points={
        "console_scripts": [
            "hos = hos:main",
        ],
    },
    author="nesnit",
    author_email="nesnit@example.com",
    description="A simple utility for managing hostnames",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YourUsername/hos-utility",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
