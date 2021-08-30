from setuptools import setup, find_packages
import os

from xpanse import __version__, __license__, __author__, __email__

try:
    description = open(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.rst")
    ).read()
except:
    description = "Please refer to https://knowledgebase.expanse.co/expander-apis/"
    print("! could not read README.rst file.")

setup(
    name="xpanse",
    version=__version__,
    description="Python library is an interface to the Xpanse Expander API.",
    author=__author__,
    long_description=description,
    author_email=__email__,
    license=__license__,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="xpanse iom",
    packages=["docs", "examples", *find_packages(exclude=["tests"])],
    install_requires=["requests>=2.23.0", "deprecated>=1.2.0"],
    include_package_data=True,
    python_requires=">=3.6",
)
