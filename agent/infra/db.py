"""
db.py

Database utilities for connecting to a SQLite database.
Provides connection management, query execution, and transaction support.
"""

import sqlite3
import threading
from typing import Any, List, Optional, Tuple

class Database:
    """
    Thread-safe SQLite database wrapper.
    """

    def __init__(self, db_path: str):
        """
        Initialize the Database with the path to the SQLite file.
        """
        self.db_path = db_path
        self._connection: Optional[sqlite3.Connection] = None
        self._lock = threading.Lock()

    def connect(self) -> sqlite3.Connection:
        """
        Open a connection to the SQLite database if not already connected.
        """
        with self._lock:
            if self._connection is None:
                self._connection = sqlite3.connect(
                    self.db_path,
                    check_same_thread=False,
                    detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
                )
                self._connection.row_factory = sqlite3.Row
            return self._connection

    def execute(self, query: str, params: Tuple[Any, ...] = ()) -> sqlite3.Cursor:
        """
        Execute a SQL statement with optional parameters.
        Returns the cursor for fetching results.
        """
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor

    def executemany(self, query: str, seq_of_params: List[Tuple[Any, ...]]) -> sqlite3.Cursor:
        """
        Execute a SQL statement against all parameter sequences provided.
        """
        conn = self.connect()
        cursor = conn.cursor()
        cursor.executemany(query, seq_of_params)
        return cursor

    def fetchall(self, cursor: sqlite3.Cursor) -> List[sqlite3.Row]:
        """
        Fetch all rows from the given cursor.
        """
        return cursor.fetchall()

    def fetchone(self, cursor: sqlite3.Cursor) -> Optional[sqlite3.Row]:
        """
        Fetch a single row from the given cursor.
        """
        return cursor.fetchone()

    def commit(self) -> None:
        """
        Commit the current transaction.
        """
        conn = self.connect()
        conn.commit()

    def rollback(self) -> None:
        """
        Roll back the current transaction.
        """
        conn = self.connect()
        conn.rollback()

    def close(self) -> None:
        """
        Close the database connection.
        """
        with self._lock:
            if self._connection:
                self._connection.close()
                self._connection = None

    def __enter__(self) -> "Database":
        """
        Context manager entry: returns self.
        """
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Context manager exit: commit or rollback depending on exception, then close.
        """
        if exc_type:
            self.rollback()
        else:
            self.commit()
        self.close()
