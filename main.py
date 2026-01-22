import api
import db
import collect_details
import collect_matches
import collect_players
import collect_ranks
import export_db


if __name__ == "__main__":
    db.init_db()
    players = collect_players.fetch_players_from_api()
    collect_players.collect_puuids(players)
    collect_matches.collect_matches()
    collect_matches.randomize_sample()
    collect_matches.match_distribution()
    collect_details.match_details()
    export_db.export_db()