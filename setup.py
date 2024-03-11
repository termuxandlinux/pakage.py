from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pakage.py",
    version="1.0.0",
    author="Alexander Krefting",
    author_email="linuxundtermux@gmail.com",
    description="An easy Pakage Programm for the most Linux Systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/termuxandlinux/pakage.py",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
