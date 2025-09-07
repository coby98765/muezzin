from datetime import datetime
import os

format_string_dt = "%Y-%m-%d %H:%M:%S"
format_string_dt_with_ms = "%Y-%m-%d %H:%M:%S.%f"

class Podcast:
    name: str
    prev_path: str
    db_id: str
    size: int
    last_open: datetime
    last_modified: datetime
    created_time: datetime

    def __init__(self,report,db_id):


        self.name = report["file_name"]
        self.prev_path = report["file_path"]
        self.db_id = str(db_id)
        self.size = report["file_size"]
        self.last_open = datetime.strptime(report["created_time"], format_string_dt)
        self.last_modified = datetime.strptime(report["last_edit_time"], format_string_dt_with_ms)
        self.created_time = datetime.strptime(report["created_time"], format_string_dt)
    def __dict__(self):
        return {
            "file_name": self.name,
            "prev_path": self.prev_path,
            "file_DB_id": self.db_id,
            "file_size": self.size,
            "created_time": self.created_time,
            "last_edit_time": self.last_modified,
            "last_open_time": self.last_open,
        }