from datetime import datetime
import os

class Podcast:
    name: str
    path: str
    size: int
    last_open: datetime
    last_modified: datetime
    created_time: datetime

    def __init__(self,path,stat):
        self.name = os.path.basename(path)
        self.path = path
        self.size = stat.st_size
        self.last_open = datetime.fromtimestamp(stat.st_atime)
        self.last_modified = datetime.fromtimestamp(stat.st_mtime)
        self.created_time = datetime.fromtimestamp(stat.st_ctime)
    def __dict__(self):
        return {
            "file_name": self.name,
            "file_path": self.path,
            "file_size": self.size,
            "created_time": str(self.created_time),
            "last_edit_time": str(self.last_modified),
            "last_open_time": str(self.last_open),
        }
    def printr(self):
        print(f"File name: {self.name}, \n"
              f"File path: {self.path}, \n"
              f"File size: {self.size}, \n"
              f"Created at: {self.created_time}, \n"
              f"Last accessed at: {self.last_open}, \n"
              f"Last modified at: {self.last_modified}.")