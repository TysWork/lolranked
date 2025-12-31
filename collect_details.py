import db
import collect_matches
import api
def fetch_match_details(match_id):
    url = f"https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}"
    response = api.request_delay(url)
    return response.json()

def match_details(limit=1):
    with db.get_connection() as conn:
        print("collecting match details...")
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS player_stats (
                match_id TEXT,
                tier TEXT,
                puuid TEXT,
                championName TEXT,
                teamPosition TEXT,
                win INTEGER,
                gameDuration INTEGER,
                kills INTEGER,
                deaths INTEGER,
                assists INTEGER,
                cs INTEGER,
                goldEarned INTEGER,
                visionScore INTEGER,
                damageDealtToChampions INTEGER,
                damageDealtToTurrets INTEGER,
                baronKills INTEGER,
                dragonKills INTEGER,
                towerKills INTEGER,
                PRIMARY KEY (match_id, puuid)
            );   
        """, )
        cur.execute(""" 
            SELECT match_id, tier FROM match_sample;
        """)
        rows = cur.fetchall()

        for i, (match_id, tier) in enumerate(rows, start=1):
            match_data = fetch_match_details(match_id)
            participants = match_data["info"]["participants"]
            team_stats = {}
            for t in match_data["info"]["teams"]:
                obj = t["objectives"]
                team_stats[t["teamId"]] = {
                    "baronKills": obj["baron"]["kills"],
                    "dragonKills": obj["dragon"]["kills"],
                    "towerKills": obj["tower"]["kills"],
                }

            game_duration = match_data["info"]["gameDuration"]
            for p in participants:
                ts = team_stats[p["teamId"]]
                cur.execute(
                    """
                    INSERT OR IGNORE INTO player_stats (
                        match_id, tier, puuid,
                        championName, teamPosition,
                        win, gameDuration, kills, deaths, assists,
                        cs, goldEarned, visionScore,
                        damageDealtToChampions,damageDealtToTurrets,
                        baronKills, dragonKills, towerKills
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        match_id,
                        tier,
                        p["puuid"],
                        p["championName"],
                        p["teamPosition"],
                        int(p["win"]),
                        game_duration,
                        p["kills"],
                        p["deaths"],
                        p["assists"],
                        p["totalMinionsKilled"] + p["neutralMinionsKilled"],
                        p["goldEarned"],
                        p["visionScore"],
                        p["totalDamageDealtToChampions"],
                        p.get("damageDealtToTurrets", 0),
                        ts["baronKills"],
                        ts["dragonKills"],
                        ts["towerKills"],
                    )
                )
            if i % 50 == 0:
                print(f"Processed {i}/{len(rows)} matches...")
            conn.commit()
        print("complete")

