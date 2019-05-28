#!/usr/bin/env python3
import argparse

def parser_args():
    """Parse args using argparse and subparsers. return parse_args()"""
    parser = argparse.ArgumentParser(
        description="""find and download the best sub for a video file""")

    parser.add_argument("filename",
                        help='''filename or text to search''',
                        type=str, nargs=1, required=True)

    parser.add_argument("-f", "--filter", nargs='+', required=False,
                              help='''filter results by text''', type=str)

    parser.add_argument("-o", "--output", nargs='1', required=False,
                              help='''define a filename for subtitle''', type=str)

    parser.add_argument("-i", "--interactive", nargs='1', required=False,
                              help='''Select interactively the subtitle''', type=str)
                              

    return parser.parse_args()
