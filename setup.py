"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="citesphere-connector",
    version="1.0.0",
    description="Connect to Citesphere, an application that enables superior management of Zotero citations",
    url="https://github.com/diging/citesphere-connector",
    author="Digital Innovation Group",
    author_email="diging@asu.edu",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Research Software Engineers, Researchers, Data Scientists, Developers",
        "Topic :: Reserach Software Engineering :: Citation Manager",
        "Programming Language :: Python",
    ],
    keywords="cite, diging, citesphere, sphere, zotero",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)
