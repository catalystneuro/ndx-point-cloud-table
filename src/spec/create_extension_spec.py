# -*- coding: utf-8 -*-

import os.path

from hdmf.spec import NamespaceBuilder, GroupSpec
from hdmf.spec.write import export_spec


def main():

    # these arguments were auto-generated from your cookie-cutter inputs
    ns_builder = NamespaceBuilder(
        doc='An extension for storing point clouds in an NWB file',
        name='ndx-point-cloud-table',
        version='0.1.0',
        author=list(map(str.strip, 'Ben Dichter'.split(','))),
        contact=list(map(str.strip, 'ben.dichter@gmail.com'.split(',')))
    )

    ns_builder.include_type('DynamicTable', namespace='hdmf-common')
    ns_builder.include_type('VectorData', namespace='hdmf-common')
    ns_builder.include_type('VectorIndex', namespace='hdmf-common')

    PointCloudTable = GroupSpec(
        doc='type for storing time-varying 3D point clouds',
        data_type_def='PointCloudTable',
        data_type_inc='DynamicTable',
        default_name='PointCloudTable'
    )

    PointCloudTable.add_dataset(
        name='timestamps',
        data_type_inc='VectorData',
        doc='time of each frame in seconds',
        dims=('num_frames',),
        shape=(None,),
        dtype='float')

    PointCloudTable.add_dataset(
        name='point_cloud',
        data_type_inc='VectorData',
        doc='datapoints locations over time',
        dims=('time', '[x, y, z]'),
        shape=(None, 3),
        dtype='float',
    )

    PointCloudTable.add_dataset(
        name='point_cloud_index',
        data_type_inc='VectorIndex',
        doc='datapoints indices',
        dims=('index',),
        shape=(None,),
    )

    PointCloudTable.add_dataset(
        name='color',
        data_type_inc='VectorData',
        doc='datapoints color',
        dims=('time', '[r, g, b]'),
        shape=(None, 3),
        dtype='float',
        quantity='?'
    )

    PointCloudTable.add_dataset(
        name='color_index',
        data_type_inc='VectorIndex',
        doc='datapoints colors indices',
        dims=('index',),
        shape=(None,),
        quantity='?'
    )

    PointCloudTable.add_attribute(
        name='colnames',
        dims=('num_columns',),
        shape=(None,),
        doc='The names of the columns in this table. This should be used to specify '
            'an order to the columns.',
        default_value=('point_cloud',),
        dtype='text'
    )

    new_data_types = [PointCloudTable]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == "__main__":
    # usage: python create_extension_spec.py
    main()
