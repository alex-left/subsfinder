import subdivx
import sys
import re
from pathlib import Path

tv_pattern = r'^(.+)([sS][0-9]{1,2}[\.\-_]?[eE][0-9]{1,2})|([0-9]{1,2}[xX][0-9]{1,2}).*'

arg = sys.argv[1]
try:
    filt = sys.argv[2]
except IndexError:
    pass

subs = subdivx.search(arg)

file = Path(arg)

tv_file = re.search(tv_pattern, file.stem)

if tv_file:
    title, episode = tv_file.groups()[:2]
    subs = subdivx.search("{} {}".format(title, episode))
else:
    subs = subdivx.search(arg)

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
chosen_subs = chosen_sub.get_subtitle()

for i, n in enumerate(chosen_subs):
    print(i, ">", n["filename"])
s = input("choice sub")
sub = chosen_subs[int(s)]
with open(file.stem+sub["extension"], "wb") as f:
    f.write(sub["data"])
