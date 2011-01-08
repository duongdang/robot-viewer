#! /usr/bin/env python

# Copyright LAAS/CNRS 2009-2012
# Authors Duong Dang
import re, sys
import vrml_parser
import robo

def parse(filename):
    re_ext = re.compile(r"\.(?P<EXT>[A-Za-z]+)$")
    m = re_ext.search(filename)
    if not m:
        raise Exception("Couldn't find file extension of %s"%filename)
    ext = m.group('EXT')
    if ext in  ["vrml","wrl"]:
        parsed_objects = vrml_parser.parse(filename)
        return parsed_objects
    else:
        raise Exception("Unknown extension %s"%ext)

if __name__ == '__main__':
    print parse(sys.argv[1])
