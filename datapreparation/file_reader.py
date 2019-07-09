import os

# https://github.com/MIT-LCP/wfdb-python
import wfdb

from signal.signal import Signal


class FileReader:

    def __init__(self, folder, database, start=''):
        self.data_folder = os.path.join(folder, database)
        self.start = start

    def __iter__(self):
        return map(self.read_file,
                   filter(lambda x: x.startswith(self.start) and x.endswith('.hea'), os.listdir(self.data_folder)))

    def read_file(self, header_name):
        path = os.path.join(self.data_folder, header_name[:-4])
        record = wfdb.rdrecord(path)
        return Signal(record)
