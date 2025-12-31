import requests 
import api
import db 

DIVISIONS = ["I","II","III","IV"]
TIERS = ["IRON","BRONZE","SILVER","GOLD","PLATINUM", "EMERALD", "DIAMOND"]

def fetch_players_from_api():
    players = []
    for tier in TIERS[:7]:
        print(f"Fetching players in tier: {tier}")
        for division in DIVISIONS:
            url = (
                f"https://na1.api.riotgames.com/"
                f"lol/league/v4/entries/RANKED_SOLO_5x5/{tier}/{division}"
                f"?page=1"
            )
            response = api.request_delay(url)
            entries = response.json()

            for player in entries:
                players.append((player['puuid'], tier, division if tier == "DIAMOND" else None))

    return players

def collect_puuids(players):
    with db.get_connection() as conn:
        cur = conn.cursor()
        print("Collecting player PUUIDs and storing in database...")
        for puuid, tier, division in players:
            cur.execute('''
                INSERT OR IGNORE INTO players (puuid, division, tier)
                        VALUES (?, ?, ?)
                ''', (puuid, division, tier))
        conn.commit()
        #cur.execute("SELECT * FROM players LIMIT 20;")
        rows = cur.fetchall()
        for row in rows:
            print(row)
