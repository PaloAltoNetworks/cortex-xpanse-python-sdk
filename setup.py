from setuptools import setup, find_packages
import os

from xpanse import __version__, __license__, __author__, __email__

try:
    description = open(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md")
    ).read()
except:
    description = "Please refer to https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference"
    print("! could not read README.md file.")

setup(
    name="xpanse",
    version=__version__,
    description="Python library is an interface to the Cortex Xpanse API.",
    author=__author__,
    long_description=description,
    long_description_content_type="text/markdown",
    author_email=__email__,
    license=__license__,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="xpanse iom",
    packages=["docs", "examples", *find_packages(exclude=["tests"])],
    install_requires=["requests>=2.25.1", "deprecated>=1.2.0", "typing_extensions>=4.5.0"],
    include_package_data=True,
    python_requires=">=3.7",
)
