from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="googol",
    description="Look up a specific index in a large JSON file with ease",
    long_description=long_description,
    license="MIT",
    author="indeedVC"
)
