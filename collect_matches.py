import db 
import api
from db import get_matches_by_tier
TIERS = ["IRON","BRONZE","SILVER","GOLD","PLATINUM", "EMERALD", "DIAMOND"]

def collect_matches():
    """ Collects ranked matches by tier. This can take a while. 
    """
    with db.get_connection() as conn:
        cur = conn.cursor()
        cur.execute('SELECT puuid FROM players;')
        print("Collecting match IDs for all players in the database...")
        puuids = cur.fetchall()
        for (puuid,) in puuids:
            url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?queue=420&start=0&count=20"
            reponse = api.request_delay(url)
            reponse.raise_for_status()
            match_ids = reponse.json()

            for match_id in match_ids:
                 cur.execute('''
                    INSERT OR IGNORE INTO matches (match_id, puuid)
                            VALUES (?, ?)
                    ''', (match_id, puuid))
        conn.commit()
    for tier, count in get_matches_by_tier():
        print(tier, count)

def randomize_sample():
    """Select a random sample of 1000 games.
    """
    with db.get_connection() as conn:
        cur = conn.cursor()
        cur.executescript("""
            DROP TABLE IF EXISTS match_sample;
                            
            CREATE TABLE match_sample (
            match_id TEXT PRIMARY KEY,
            tier TEXT
            );
        """)
        for tier in TIERS:

            cur.execute("""
                INSERT OR IGNORE INTO match_sample (match_id, tier)
                SELECT m.match_id, p.tier
                FROM matches m
                JOIN players p ON p.puuid = m.puuid
                WHERE p.tier = ?
                ORDER BY RANDOM()
                LIMIT 1000;
            """, (tier,))
        cur.execute("SELECT tier, COUNT(*) FROM match_sample GROUP BY tier;")
        print(cur.fetchall())

        conn.commit()
        
def match_distribution(min = 1000):
    """Guarantees there are at least 1000 games in each tier.
    """
    counts = get_matches_by_tier()
    for tier, count in counts:
        if count < min:
            raise ValueError(f"{tier} only has {count} matches.")
        