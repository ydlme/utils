# -*- coding: utf-8 -*-

import os

def walk_with_filter(rootdir, filters, target_list):
    res = os.walk(rootdir)
    def path_of(root, fname):
        return os.path.join(root, fname)

    for root, dirs, files in res:
        target = [path_of(root, fname) for fname in files
                if any(item in fname for item in filters)]
        target_list.extend(target)



if __name__ == '__main__':
    source_file = []
    filters = ['.cpp', '.h']
    target_dir = '/home/justin/libtnet'
    walk_with_filter(target_dir, filters, source_file)
    
    command = 'vim -me -e -c ":hardcopy >%.ps" -c ":q" '
    for fname in source_file:
        os.system(command + fname)
    
    for fname in source_file:
        os.system("ps2pdf {0}.ps {0}.pdf".format(fname))
        os.remove("{0}.ps".format(fname))

