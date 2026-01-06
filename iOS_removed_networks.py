#! /usr/bin/env python
import sys
from optparse import OptionParser
import plistlib


if sys.version_info[0] < 3:
    print("Must be using Python 3! Exiting.")
    exit(-1)

usage = "\n%prog -i inputfile\n"

parser = OptionParser(usage=usage)
parser.add_option("-i", dest="inputfile", 
                  action="store", type="string",
                  help="\private\var\mobile\Library\Preferences\com.apple.wifi.removed-networks.plist")             
(options, args) = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help()
    exit(-1)

with open(options.inputfile, 'rb', ) as fp:
    pl = plistlib.load(fp, dict_type=dict)
    if pl.items():
        for key, list1 in pl.items():
            print("==================================")
            print(key)
            for item, list1 in pl[key].items():
                if item == "CaptiveProfile":
                    print("CaptiveProfile:")
                    for item2 in list1:
                        print("  - " + item2 + ": " + str(list1[item2]))
                else:
                    print(item + " : " + str(list1))
