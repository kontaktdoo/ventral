from setuptools import setup, find_packages

setup(
    name="ventral",  # Change this from "ventral-api-client" to "ventral"
    version="0.1.2",  # Increment the version
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
