import sqlite3

CONN = sqlite3.connect(":memory:")


def configure_db() -> None:
    cur: sqlite3.Cursor = CONN.cursor()
    cur.execute(
        """
CREATE TABLE IF NOT EXISTS table_of_counts (
    session_id text,
    actual_count
)
    """
    )

    cur.execute(
        "INSERT INTO table_of_counts (session_id, actual_count) VALUES (?,?)",
        ("dummy session", 0),
    )


def get_call_count(sess_id: str = "dummy session") -> int:
    cur: sqlite3.Cursor = CONN.cursor()
    cur.execute(
        "SELECT actual_count FROM table_of_counts WHERE session_id = ?", (sess_id,)
    )
    return cur.fetchone()[0]


def increament_call_count(sess_id: str = "dummy session") -> int:
    count: int = get_call_count(sess_id)
    count += 1
    cur: sqlite3.Cursor = CONN.cursor()
    cur.execute(
        "UPDATE table_of_counts SET actual_count = ? WHERE session_id = ?",
        (
            count,
            sess_id,
        ),
    )
    return count
