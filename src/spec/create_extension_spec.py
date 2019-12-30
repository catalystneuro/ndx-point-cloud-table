# -*- coding: utf-8 -*-

import os.path

from pynwb.spec import NWBNamespaceBuilder, export_spec, NWBGroupSpec, NWBAttributeSpec
# TODO: import the following spec classes as needed
# from pynwb.spec import NWBDatasetSpec, NWBLinkSpec, NWBDtypeSpec, NWBRefSpec


def main():
    # these arguments were auto-generated from your cookie-cutter inputs
    ns_builder = NWBNamespaceBuilder(
        doc='An extension for storing point clouds in an NWB file',
        name='ndx-point-cloud-table',
        version='0.1.0',
        author=list(map(str.strip, 'Ben Dichter'.split(','))),
        contact=list(map(str.strip, 'ben.dichter@gmail.com'.split(',')))
    )

    PointCloudTable = NWBGroupSpec(
        doc='type for storing time-varying 3D point clouds',
        neurodata_type_def='PointCloudTable',
        neurodata_type_inc='DynamicTable',
    )

    PointCloudTable.add_dataset(
        name='point_cloud',
        neurodata_type_inc='VectorData',
        doc='datapoints locations over time',
        dims=('time', '[x, y, z]'),
        shape=(None, 3),
        dtype='float',
    )

    PointCloudTable.add_dataset(
        name='point_cloud_index',
        neurodata_type_inc='VectorIndex',
        doc='datapoints indices',
        dims=('index',),
        shape=(None,),
    )

    PointCloudTable.add_dataset(
        name='color',
        neurodata_type_inc='VectorData',
        doc='datapoints color',
        dims=('time', '[r, g, b]'),
        shape=(None, 3),
        dtype='float',
        quantity='?'
    )

    PointCloudTable.add_dataset(
        name='color_index',
        neurodata_type_inc='VectorIndex',
        doc='datapoints colors indices',
        dims=('index',),
        shape=(None,),
        quantity='?'
    )

    new_data_types = [PointCloudTable]

    ns_builder.include_type('DynamicTable', namespace='hdmf-common')
    ns_builder.include_type('VectorData', namespace='hdmf-common')
    ns_builder.include_type('VectorIndex', namespace='hdmf-common')

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == "__main__":
    # usage: python create_extension_spec.py
    main()
