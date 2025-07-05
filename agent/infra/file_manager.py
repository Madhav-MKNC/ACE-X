"""
file_manager.py

Utilities for filesystem operations: reading, writing, and organizing files/directories.
"""

import os
from typing import Any, Dict, List

class FileManager:
    """
    Provides high-level file system operations for the agent.
    """

    @staticmethod
    def read_text(path: str) -> str:
        """
        Read and return the contents of a text file.
        """
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    @staticmethod
    def write_text(path: str, content: str) -> None:
        """
        Write text content to a file, creating directories if needed.
        """
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

    @staticmethod
    def list_files(directory: str, extensions: List[str] = None) -> List[str]:
        """
        List files in a directory optionally filtered by extensions.
        """
        files = []
        for root, _, filenames in os.walk(directory):
            for name in filenames:
                if extensions is None or any(name.endswith(ext) for ext in extensions):
                    files.append(os.path.join(root, name))
        return files

    @staticmethod
    def delete(path: str) -> None:
        """
        Delete a file or directory.
        """
        if os.path.isdir(path):
            for root, dirs, files in os.walk(path, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(path)
        elif os.path.exists(path):
            os.remove(path)
