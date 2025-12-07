from setuptools import setup , find_packages

setup(
    name="document_portal",
    author="Mahmoud Mohamed",
    version="0.1",
    packages=find_packages() # will look for folders with __init__.py any other folder wont be considered in the package
)