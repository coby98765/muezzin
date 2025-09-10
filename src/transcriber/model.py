from datetime import datetime
import os

format_string_dt_with_ms = "%Y-%m-%d %H:%M:%S.%f"

class Podcast:
    name: str
    file_path: str
    size: int
    transcript:str
    last_open: datetime
    last_modified: datetime
    created_time: datetime

    def __init__(self,report):
        self.name = report["file_name"]
        self.file_path = report["file_path"]
        self.size = report["file_size"]
        self.last_open = datetime.strptime(report["created_time"], format_string_dt_with_ms)
        self.last_modified = datetime.strptime(report["last_edit_time"], format_string_dt_with_ms)
        self.created_time = datetime.strptime(report["created_time"], format_string_dt_with_ms)

    def add_transcript(self,text):
        self.transcript = text

    def __dict__(self):
        return {
            "file_name": self.name,
            "file_path": self.file_path,
            "file_size": self.size,
            "transcript": self.transcript,
            "created_time": str(self.created_time),
            "last_edit_time": str(self.last_modified),
            "last_open_time": str(self.last_open),
        }