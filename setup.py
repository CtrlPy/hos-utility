from setuptools import setup, find_packages
import pathlib

# Директория проекта
HERE = pathlib.Path(__file__).parent

# Читаем содержимое файла README.md
long_description = (HERE / "README.md").read_text()

setup(
    name="hos-utility",
    version="0.0.1",
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
    long_description_content_type="text/markdown",  # Використовуємо Markdown для довгого опису
    url="https://github.com/YourUsername/hos-utility",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
