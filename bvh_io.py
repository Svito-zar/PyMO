# This code was written by Taras Kucherenko:
"""
This script can read, crop and write a BVH file
"""

from argparse import ArgumentParser

import os
import sys

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from pymo.parsers import BVHParser
from pymo.writers import *


def extract_joint_angles(in_file, out_file, start_t, end_t, fps):
    p = BVHParser()

    print("Reading ...")
    data_all = list()
    data_all.append(p.parse(in_file))

    print("Cropping ...")
    cropped_data = data_all[0]
    cropped_data.values = cropped_data.values
    if end_t == -1:
        cropped_data.values = cropped_data.values[start_t * fps:]
    else:
        cropped_data.values = cropped_data.values[start_t * fps: end_t * fps]

    print("Writing ...")
    writer = BVHWriter()
    with open(out_file,'w') as f:
        writer.write(cropped_data, f)



if __name__ == '__main__':

    # Setup parameter parser
    parser = ArgumentParser(add_help=False)
    parser.add_argument('--in_file', '-orig', required=True,
                        help="Path where original motion file (in BVH format) is stored")
    parser.add_argument('--out_file', '-dest', required=True,
                        help="Path where extracted motion file will be stored")
    parser.add_argument('--start_t', '-st', required=False, default=0, type=int,
                        help="Starting time for the new bvh file (in seconds)")
    parser.add_argument('--end_t', '-end', required=False, default=60, type=int,
                        help="Ending time for the new bvh file (in seconds)")

    params = parser.parse_args()

    extract_joint_angles(params.in_file, params.out_file, params.start_t, params.end_t, 60)