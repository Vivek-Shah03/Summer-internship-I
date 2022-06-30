import gzip
import shutil
with open('temp.txt', 'rb') as f_in, gzip.open('temp.txt.gz', 'wb') as f_out:
    shutil.copyfileobj(f_in, f_out)