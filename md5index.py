#given a folder path, makes a hash index of every file, recursively
import sys, os, hashlib, io

hash_md5 = hashlib.md5()

#some files need to be hashed incrementally as they may be too big to fit in memory
#http://stackoverflow.com/a/40961519/2518451
def md5sum(src, length=io.DEFAULT_BUFFER_SIZE):
    md5 = hashlib.md5()
    with io.open(src, mode="rb") as fd:
        for chunk in iter(lambda: fd.read(length), b''):
            md5.update(chunk)
    return md5

#this project done on macOS. There may be other files that are appropriate to hide on other platforms.
ignore_files = [".DS_Store"]

def index(source, index_output):

    index_output_f = open(index_output, "wt")
    index_count = 0
    
    for root, dirs, filenames in os.walk(source):

        for f in filenames:
            if f in ignore_files:
                continue
            
            #print f
            fullpath = os.path.join(root, f)
            #print fullpath
            
            md5 = md5sum(fullpath)
            md5string = md5.hexdigest()
            line = md5string + ":" + fullpath
            index_output_f.write(line + "\n")
            print line
            index_count += 1
            
    index_output_f.close()
    print("Index Count: " + str(index_count))

    
if __name__ == "__main__":
    index_output = "index_output.txt"
    
    if len(sys.argv) < 2:
        print("Usage: md5index [path]")
    else:
        index_path = sys.argv[1]
        print("Indexing... " + index_path)
        index(index_path, index_output)
        
