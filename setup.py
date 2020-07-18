'''
@Author: Zitian(Daniel) Tong
@Date: 2020-07-17 17:38:54
@LastEditTime: 2020-07-17 17:43:47
@LastEditors: Zitian(Daniel) Tong
@Description: setup files from pypi
@FilePath: /yogurt/setup.py
'''
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yogurt", # Replace with your own username
    version="0.0.1",
    author="Zitian(Daniel) Tong",
    author_email="danieltongubc@gmail.com",
    description="A package to simplify the imteraction with smart contract",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DanielTongAwesome/yogurt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5.6',
)