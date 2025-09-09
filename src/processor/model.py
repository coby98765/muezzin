from datetime import datetime

format_string_dt = "%Y-%m-%d %H:%M:%S"
format_string_dt_with_ms = "%Y-%m-%d %H:%M:%S.%f"


class Podcast:
    _id:str
    name: str
    file_path: str
    size: int
    transcript:str
    bds_percent:int
    is_bds:bool
    bds_threat_level:str
    last_open: datetime
    last_modified: datetime
    created_time: datetime

    def __init__(self,report,_id):
        self._id = _id
        self.name = report["file_name"]
        self.file_path = report["file_path"]
        self.size = report["file_size"]
        self.transcript = report["transcript"]
        self.last_open = datetime.strptime(report["created_time"], format_string_dt)
        self.last_modified = datetime.strptime(report["last_edit_time"], format_string_dt_with_ms)
        self.created_time = datetime.strptime(report["created_time"], format_string_dt)

    def __dict__(self):
        return {
            "_id":self._id,
            "file_name": self.name,
            "file_path": self.file_path,
            "file_size": self.size,
            "transcript":self.transcript,
            "created_time": self.created_time,
            "last_edit_time": self.last_modified,
            "last_open_time": self.last_open,
        }
    @staticmethod
    def map():
        return {
            "file_name": {"type": "keyword"},
            "file_path": {"type": "keyword"},
            "file_size": {"type": "int"},
            "transcript":{"type": "text"},
            "created_time": {"type": "date"},
            "last_edit_time": {"type": "date"},
            "last_open_time": {"type": "date"},
        }