import sqlite3
DB_PATH = "league.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    try:
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS players (
                    puuid TEXT PRIMARY KEY,
                    division TEXT,
                    tier TEXT
                );
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS matches (
                    match_id TEXT PRIMARY KEY,
                    puuid TEXT
                );
            """)
        print("Database initialized.")
        return True
    except Exception as e:
        print("ERROR: Database init failed:", e)
        return False
    
def get_matches_by_tier():
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT p.tier, COUNT(*) AS match_count
            FROM matches m
            JOIN PLAYERS p ON p.puuid = m.puuid
            GROUP BY p.tier 
            ORDER BY match_count DESC;
        """)
        return cur.fetchall()
    