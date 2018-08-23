#! /usr/bin/env python

import os
import private.metadata as metadata

from make_logs import make_stats_log, make_heads_log
from private.linkslist import LinksList

def make_link_logs(link_dict,
                   link_statslog = metadata.settings['link_statslog'],, 
                   link_headslog = metadata.settings['link_headslog'],
                   link_maplog = metadata.settings['link_maplog'],
                   recursive = float('inf')):     
    
    target_list = link_dict.keys()
    target_list = [glob_recursive(t, recursive) for target in target_list]
    target_files = [f for target in target_list for f in target]

    make_statslog(link_statslog, target_files)
    make_headslog(link_headslog, target_files)    
    make_link_maplog(link_maplog, link_dict)
    

def make_link_maplog(link_maplog, link_dict):

    header = 'target\tsymlink'

    with open(link_maplog, 'w+') as MAPLOG:
        print >> MAPLOG, header  

        for k, v in link_dict.items()
            print >> MAPLOG, "%s\t%s" % (k, v)
        
      
