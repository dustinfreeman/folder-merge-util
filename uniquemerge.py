#given an index_output.txt in the same directory and an input path,
#remove all files that already have a hash in index_output.txt

import sys, os
from md5index import md5sum
from send2trash import send2trash
SENDING_TO_TRASH = True

def load_index():
    index_output = "index_output.txt"
    index = []
    with open(index_output, "rt") as index_output_f:
        for line in index_output_f:
            line_split = line.split(':')
            md5 = line_split[0]
            index.append(md5)
    return index
            
#traverse file, compare against index
def traverse_merge_path(merge_path, index):
    found = 0
    not_found = 0
    
    for root, dirs, filenames in os.walk(merge_path):
        for f in filenames:
            #print f
            fullpath = os.path.join(root, f)
            #print fullpath
            
            md5 = md5sum(fullpath)
            md5string = md5.hexdigest()

            if md5string in index:
                if SENDING_TO_TRASH:
                    send2trash(fullpath)
                
                found += 1
            else:
                print "\t NON-DUPLICATE ORIGINAL: " + fullpath
                not_found += 1
                

    print "Found Duplicates: " + str(found) + " Originals: " + str(not_found)


if __name__ == "__main__":
    index = load_index()
    print "Loaded index with item count: " + str(len(index))

    print "SENDING_TO_TRASH: " + str(SENDING_TO_TRASH) 
    
    merge_path = sys.argv[1]
    print "Merging To: " + merge_path
    
    traverse_merge_path(merge_path, index)


    



