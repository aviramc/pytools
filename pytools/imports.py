import os.path
import imp

def path_import(filename):
    module_name = os.path.basename(os.path.splitext(filename)[0])
    return imp.load_source(module_name, filename)

