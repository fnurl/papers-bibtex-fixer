#!/usr/bin/env python
#coding=UTF-8

import sys
import codecs
import getopt
import re

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "h", ["help"])
        filename = args[0]
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    except IndexError:
        print 'Please supply a filename.'
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()

    try:
        original_file = codecs.open(filename, encoding='utf-8', mode='r')

        for line in original_file:
            # e.g. Castellv{\'\i} → Castellv{\'i}
            line = re.sub(r'{\\([\'])\\([A-Za-z]{1,2})}', r'{\\\1\2}', line)
            # e.g. Castellv{\'i} → Castellv\'{i}
            line = re.sub(r'{\\([`\'\^"~=.uvHtcdb][ ]*)([A-Za-z]{1,2})}', r'\\\1{\2}', line)
            # e.g. Tufi\c {s} → Tufi\c{s}
            line = re.sub(r'\\([uvHtcdb]) *', r'\\\1', line)
            # preserve capitalization
            if line.startswith('publisher') or line.startswith('journal') or line.startswith('title') or line.startswith('booktitle'):
                line = re.sub(r'([A-Z]+)', r'{\1}', line)
            sys.stdout.write(line.encode('utf-8'))
        original_file.close()
    except IOError:
        print "IOError."
        sys.exit(2)


def usage():
    print '''USAGE: fixbib.py [options] <filename>
       Fixes BibTeX output from Papers 2: Corrects escapes and preserves capitalizations.

       -h    help'''

if __name__ == "__main__":
    main(sys.argv[1:])
