#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from pisces_deps import version

install_requires = []

with open('requirements.txt', 'r') as f:
    for req in f.readlines():
        install_requires.append(req.strip('\n'))


setup(
    name='pisces_deps',
    version=version,
    url='https://github.com/wuyue92tree/pisces_deps',
    description='pisces依赖，用于树莓派gpio传感器控制',
    long_description=open('README.md').read(),
    author='wuyue',
    author_email='wuyue92tree@163.com',
    maintainer='wuyue',
    maintainer_email='wuyue92tree@163.com',
    license='MIT',
    packages=find_packages(exclude=('tests', 'tests.*')),
    include_package_data=True,
    zip_safe=False,
    entry_points={},
    install_requires=install_requires,
)