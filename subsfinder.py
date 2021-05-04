#!/usr/bin/python3
import subdivx
import re
import argparse
from pathlib import Path

tv_pattern = r'^(.+)([sS][0-9]{1,2}[\.\-_]?[eE][0-9]{1,2})|([0-9]{1,2}[xX][0-9]{1,2}).*'


def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("search", type=str)
    parser.add_argument("-o", "--output", type=str, default=None)
    parser.add_argument("-f", "--filter", type=str, default=None)
    return parser.parse_args()


args = argparser()
file_to_search = args.search
filt = args.filter
output = args.output

input_file = Path(file_to_search)

tv_file = re.search(tv_pattern, input_file.stem)

if tv_file:
    title, episode = tv_file.groups()[:2]
    subs = subdivx.search("{} {}".format(title, episode))
else:
    print("entra")
    subs = subdivx.search(file_to_search)

subs = sorted(subs, key=lambda x: x.downloads, reverse=True)

for i, sub in enumerate(subs):
    if filt:
        if filt.lower() in sub.description.lower():
            print(i, "> ", sub.title, "** ", sub.downloads)
            print("\t", sub.description)
    else:
        print(i, "> ", sub.title, "** ", sub.downloads)
        print("\t", sub.description)


choice = input("choose an option ")

chosen_sub = subs[int(choice)]
chosen_subs = chosen_sub.get_subtitles()

for i, n in enumerate(chosen_subs):
    print(i, ">", n["filename"])
s = input("choice sub")
sub = chosen_subs[int(s)]

if output:
    output_file = output
else:
    output_file = input_file.stem
with open(output_file+sub["extension"], "wb") as f:
    f.write(sub["data"])
