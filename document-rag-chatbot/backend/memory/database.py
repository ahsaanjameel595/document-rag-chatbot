import sqlite3
from pathlib import Path


DB_PATH = Path("chat_history.db")


def get_connection():

    connection = sqlite3.connect(
        DB_PATH,
        check_same_thread=False,
    )

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT NOT NULL,
            role TEXT NOT NULL,
            content TEXT NOT NULL
        )
        """
    )

    connection.commit()

    return connection


def save_message(
    session_id: str,
    role: str,
    content: str,
):

    connection = get_connection()

    connection.execute(
        """
        INSERT INTO messages
        (session_id, role, content)
        VALUES (?, ?, ?)
        """,
        (
            session_id,
            role,
            content,
        ),
    )

    connection.commit()

    connection.close()


def get_messages(session_id: str):

    connection = get_connection()

    cursor = connection.execute(
        """
        SELECT role, content
        FROM messages
        WHERE session_id = ?
        ORDER BY id
        """,
        (session_id,),
    )

    messages = cursor.fetchall()

    connection.close()

    return messages


def clear_session(session_id: str):

    connection = get_connection()

    connection.execute(
        """
        DELETE FROM messages
        WHERE session_id = ?
        """,
        (session_id,),
    )

    connection.commit()

    connection.close()