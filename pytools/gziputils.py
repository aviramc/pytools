from cStringIO import StringIO
from gzip import GzipFile

def gunzip_string(string):
    gzip_reader = GzipFile(fileobj=StringIO(string), mode='rb')
    return gzip_reader.read()

def gzip_string(string):
    gzipped_file = StringIO()
    gzip_writer = GzipFile(fileobj=gzipped_file, mode='w')
    gzip_writer.write(string)
    gzip_writer.close()
    gzipped_file.seek(0)
    return gzipped_file.read()
