"""Manage the storage, reload objects of the last execution"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
