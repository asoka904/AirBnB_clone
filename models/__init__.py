from .engine.file_storage import FileStorage
"""Manage the storage, reload objects of the last execution"""

storage = FileStorage()
storage.reload()
