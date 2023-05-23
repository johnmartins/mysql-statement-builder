from setuptools import setup

setup(
    name='mysql-statement-builder',
    version='0.2.0',
    description='Simplifies writing MySQL statements in non-ORM environments.',
    py_modules=["mysqlsb"],
    package_dir={'': 'mysqlsb'}
)
