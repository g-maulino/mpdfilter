#!/usr/bin/env python3
#
# main DASH - parse MPEG DASH manifest and remove specified attributes
#
#            input: Manifest URL
#           output: Manifest without attributes=value spec
#
# Author: g-maulino
#

import os
import re
import sys
import xml.etree.ElementTree as etree
from optparse import OptionParser
from mpegdash.parser import MPEGDASHParser
import urllib.request
import urllib.error
import urllib.parse

class MPDattfilter:

    def __init__(self):
        
        self.data = None

    def get_dash(self,data):
        """ Returns the filtered manifest """

        mpd_str = data #str(data, 'utf-8')
        mpd = MPEGDASHParser.parse(mpd_str)

        # check success and basic control (not null + MPD format)
        if mpd is None or not mpd:
            return None
                
        for period in mpd.periods:
            for adapt_set in period.adaptation_sets:
                for rep_set in adapt_set.representations:
                    if( rep_set.segment_templates is not None):
                        for rep_temp in rep_set.segment_templates:
                            for seg in rep_temp.segment_timelines:
                                for i in range(len(seg.Ss)):
                                    print("seg: " + seg.Ss[i])
                            #for seg in rep_temp.segment_timelines.S:
                            #    print("seg: " + seg.t)
       

        MPEGDASHParser.write(mpd, 'new_mpd.mpd')

        return True
            
    def filter_r0(self,data):
        """ Returns the filtered manifest """

        mpd_str = str(data, 'utf-8')
        mpd = MPEGDASHParser.parse(mpd_str)

        # check success and basic control (not null + MPD format)
        if mpd is None or not mpd:
            return None
                
        for period in mpd.periods:
            for adapt_set in period.adaptation_sets:
                for rep_set in adapt_set.representations:
                    if( rep_set.segment_templates is not None):
                        for rep_temp in rep_set.segment_templates:
                            for seg in rep_temp.segment_timelines:
                                for i in range(len(seg.Ss)):
                                    if( seg.Ss[i].r == 0 ):
                                       # remove r attribute in S entry when r=0
                                       seg.Ss[i].r = None

        xmlstrout = MPEGDASHParser.toprettyxml(mpd)
        print(xmlstrout)

        return xmlstrout.encode()
        
def main() -> int:
    """Echo the input arguments to standard output"""
    with open(sys.argv[1], 'r') as my_file:
        data = my_file.read()
        get_dash(data)

    return 0

if __name__ == '__main__':
    sys.exit(main())  #