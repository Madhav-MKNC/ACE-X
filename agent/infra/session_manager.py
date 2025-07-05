"""
session_manager.py

Utilities for managing persistent session data between agent runs.
Stores and retrieves key-value session state as JSON on disk.
"""

import os
import json
from threading import Lock
from typing import Any, Dict

class SessionManager:
    """
    Thread-safe manager for session persistence.
    """

    def __init__(self, session_file: str):
        """
        Initialize the SessionManager with the path to the JSON session file.
        """
        self.session_file = session_file
        self._lock = Lock()
        self._session_data: Dict[str, Any] = {}

    def load(self) -> Dict[str, Any]:
        """
        Load session data from the session_file.
        Returns the session dictionary.
        """
        with self._lock:
            if os.path.exists(self.session_file):
                with open(self.session_file, 'r', encoding='utf-8') as f:
                    self._session_data = json.load(f)
            else:
                self._session_data = {}
            return self._session_data

    def save(self) -> None:
        """
        Save current session data to the session_file.
        """
        with self._lock:
            os.makedirs(os.path.dirname(self.session_file), exist_ok=True)
            with open(self.session_file, 'w', encoding='utf-8') as f:
                json.dump(self._session_data, f, indent=2)

    def get(self, key: str, default: Any = None) -> Any:
        """
        Retrieve a value from the session data.
        """
        with self._lock:
            return self._session_data.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """
        Set a value in the session data and persist immediately.
        """
        with self._lock:
            self._session_data[key] = value
            self.save()

    def clear(self) -> None:
        """
        Clear all session data and remove the session file.
        """
        with self._lock:
            self._session_data.clear()
            if os.path.exists(self.session_file):
                os.remove(self.session_file)
