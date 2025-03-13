from setuptools import setup, find_packages
import pathlib

# Read the README file with explicit UTF-8 encoding
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="ventral",  # Change this from "ventral-api-client" to "ventral"
    version="0.1.4",  # Increment the version
    packages=find_packages(),
    install_requires=[],  # List dependencies here
    author="Bare Luka Zagar",
    author_email="bare@ventral.ai",
    description="A client for Ventral Vision AI's API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kontaktdoo/ventral",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
