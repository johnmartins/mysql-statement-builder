from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='mysql-statement-builder',
    version='0.2.1',
    description='Simplifies writing MySQL statements in non-ORM environments.',
    py_modules=["mysqlsb"],
    package_dir={'': 'mysqlsb'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    extras_require={
        "dev": [
            "pytest>=7.3",
            "twine>=4.0"
        ]
    }
)
