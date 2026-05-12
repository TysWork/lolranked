# League of Legends Ranked Stats Pipeline

A Python data pipeline for collecting, storing, and analyzing ranked League of Legends match data using the Riot Games API.

The goal of this project is to compare ranked player performance across tiers from Iron through Diamond by collecting match data, transforming it into a structured database, and preparing it for SQL analysis and dashboard visualization.

---

## Project Overview

This project collects ranked League of Legends data from the Riot API and stores it locally in SQLite. The pipeline gathers player identifiers, retrieves recent ranked solo queue matches, extracts participant-level match statistics, and exports the final dataset for analysis.

The project is designed as a data analytics / data engineering portfolio project, with a focus on:

- Working with a real-world public API
- Handling API rate limits
- Designing a repeatable data collection pipeline
- Structuring semi-structured JSON data into relational tables
- Preparing clean data for SQL, Python, and Tableau analysis
  
---

## Business / Analysis Questions

This project is built around the question:

> How do ranked League of Legends performance metrics change as players move from lower ranks to higher ranks?

Some questions this dataset can help answer include:

- How do kills, deaths, assists, and KDA differ by ranked tier?
- Do higher-ranked players average more gold, CS, and vision score?
- How does damage to champions vary across ranks?
- Are objective-related stats such as dragon, baron, and tower kills higher in higher ranks?
- Which roles show the biggest performance differences between tiers?

---

## Current Features

The current pipeline supports:

- Fetching ranked player PUUIDs by tier and division
- Collecting ranked solo queue match IDs for each player
- Sampling matches by tier to create a balanced dataset
- Fetching detailed match data from the Riot Match API
- Extracting participant-level statistics
- Storing data in a local SQLite database
- Exporting the final `player_stats` table to CSV

---

## Data Collected

The final player-level dataset includes fields such as:

| Column | Description |
|---|---|
| `match_id` | Unique Riot match identifier |
| `tier` | Ranked tier associated with the sampled player |
| `puuid` | Player unique identifier |
| `championName` | Champion played |
| `teamPosition` | Role / position played |
| `win` | Whether the participant won the match |
| `gameDuration` | Match duration in seconds |
| `kills` | Player kills |
| `deaths` | Player deaths |
| `assists` | Player assists |
| `cs` | Total minions + neutral monsters killed |
| `goldEarned` | Total gold earned |
| `visionScore` | Player vision score |
| `damageDealtToChampions` | Total champion damage dealt |
| `damageDealtToTurrets` | Total turret damage dealt |
| `baronKills` | Team baron kills |
| `dragonKills` | Team dragon kills |
| `towerKills` | Team tower kills |

---
## Tableau Visualization

https://public.tableau.com/views/LeagueRanks/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

## Project Structure

```text
lolranked/
├── api.py                 # Riot API request helper and rate-limit handling
├── db.py                  # SQLite connection and database setup
├── main.py                # Main pipeline entry point
├── collect_players.py     # Collect ranked player PUUIDs
├── collect_matches.py     # Collect match IDs and create tier samples
├── collect_details.py     # Fetch match details and extract player stats
├── collect_ranks.py       # Placeholder for future rank-related logic
├── export_db.py           # Export player_stats table to CSV
├── lol.ipynb              # Notebook for exploration / analysis
├──League Ranks.twbx       # Tableau Workbook to visualize stat differences each rank
└── README.md
