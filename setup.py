import os

from setuptools import setup


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name="runnn",
    version="0.1",
    author="Peter Izsak",
    author_email="peteriz@gmail.com",
    description=(
        "A utility to run python script with multiple arguments using a yaml configuration."
    ),
    license="MIT",
    keywords="yaml arguments runner",
    url="https://github.com/peteriz/runnn",
    packages=[
        "runnn",
    ],
    scripts=[
        "bin/runnn",
    ],
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
