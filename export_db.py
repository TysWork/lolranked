import sqlite3
import csv
import pandas as pd


DB_PATH = 'league.db'
TABLE_NAME = 'player_stats'

def export_db():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(f'SELECT * FROM {TABLE_NAME}', conn)
    df.to_csv('player_stats_export.csv', index=False)
    conn.close()