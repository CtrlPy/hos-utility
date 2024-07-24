from setuptools import setup, find_packages

setup(
    name="hos-utility",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "urwid",
    ],
    entry_points={
        "console_scripts": [
            "hos = hos:main",
        ],
    },
    author="Ваше ім’я",
    author_email="ваша_пошта@example.com",
    description="A simple utility for managing hostnames",
    url="https://github.com/YourUsername/hos-utility",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
