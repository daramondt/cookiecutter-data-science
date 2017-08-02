from setuptools import setup, find_packages
import os,os.path
curfilePath = os.path.abspath(__file__)
curDir = os.path.abspath(os.path.join(curfilePath,os.pardir))
dirName = curDir.split('/')[-1]

setup(
    name=dirName,
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'pandas>=0.19.*'
    ],
)
