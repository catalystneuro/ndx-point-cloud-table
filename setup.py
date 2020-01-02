# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages
from shutil import copy2

with open('README.md', 'r') as fp:
    readme = fp.read()

setup_args = {
    'name': 'ndx-point-cloud-table',
    'version': '0.1.0',
    'description': 'An extension for storing point clouds in an NWB file',
    'long_description': readme,
    'long_description_content_type': 'text/markdown',
    'author': 'Ben Dichter',
    'author_email': 'ben.dichter@gmail.com',
    'url': 'https://github.com/ben-dichter-consulting/ndx-point-cloud-table',
    'license': 'BSD 3-Clause',
    'install_requires': ['open3d', 'pynwb'],
    'packages': find_packages('src/pynwb'),
    'package_dir': {'': 'src/pynwb'},
    'package_data': {'ndx_point_cloud_table': [
        'spec/ndx-point-cloud-table.namespace.yaml',
        'spec/ndx-point-cloud-table.extensions.yaml',
    ]},
    'classifiers': [
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
    ],
    'zip_safe': False
}


def _copy_spec_files(project_dir):
    ns_path = os.path.join(project_dir, 'spec', 'ndx-point-cloud-table.namespace.yaml')
    ext_path = os.path.join(project_dir, 'spec', 'ndx-point-cloud-table.extensions.yaml')

    dst_dir = os.path.join(project_dir, 'src', 'pynwb', 'ndx_point_cloud_table', 'spec')
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)

    copy2(ns_path, dst_dir)
    copy2(ext_path, dst_dir)


if __name__ == '__main__':
    _copy_spec_files(os.path.dirname(__file__))
    setup(**setup_args)
