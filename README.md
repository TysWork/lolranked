# League of Legends Ranked Stats Pipeline (WIP)

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

## Key Findings 

- **Core farming and economy metrics improved with rank.** CS per minute and gold per minute generally increased from Iron through diamond, which suggests that higher-ranked players convert time into resources more efficienctly.
- **Vision control imrpoved across ranks, then began to fall level out.** Average vision score rose from lower ranks into higher ranks, showing more map awareness and vision control among higher-ranked players.
- **Combat stats were not as linear as economy stats.** While kills and deaths did not trend upwards, assists did. Suggesting that higher ranks are better at team involvement and more optimal decision-making rather than focusing on individual impact.
- **Objective control peaks at peaks in the middle tier ranks.** Dragon and Baron kills trend upwards, peaking at Gold before dropping at Diamond. This may reflect sample size limitations, role differences, or likely more contested objective setups at higher levels.
- **Role filtering shows meaningful difference in playstyle.** The dashboard allows users to compare performance metrics by role, highlighting differences in kill participation, vision control, economy, and objective control through all ranks.
---

## Current Features

The current pipeline supports:

- Fetching ranked player PUUIDs by tier and division
- Collecting ranked solo queue match IDs for each player
- Sampling matches by tier to create a balanced dataset
- Fetching detailed match data from the Riot Match API
- Extracting participant-level statistics
- Storing data in a local SQLite database
- Export raw player stats to `player_stats_export.csv`
- Create or use a processed analysis file, `ps_export.csv`, with derived metrics for Tableau

---

## Data Collected
### Exported Data Files

The pipeline exports the raw `player_stats` table as text

player_stats_export.csv

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
├── League Ranks.twbx      # Tableau workbook for visualizing rank stat differences
└── README.md
```

## Tableau Dashboard

A Tableau dashboard was created to visualize ranked League of Legends performance trends across tiers and roles.

View the dashboard here: [League of Legends Ranked Dashboard](https://public.tableau.com/views/LeagueofLegendsRankedPerformanceDashboard/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

The dashboard focuses on questions such as:

- How do performance metrics change across ranked tiers?
- Which roles have the largest differences between ranks?
- How do CS/min, gold/min, damage/min, vision score, and kill participation compare by tier?
- Are objective-related stats higher in higher ranks?

### Dashboard Metrics

The dashboard uses derived metrics from the processed analysis file, including:

| Metric | Description |
|---|---|
| `cs_per_minute` | Creep score normalized by match length |
| `gold_per_minute` | Gold earned normalized by match length |
| `damage_per_minute` | Champion damage normalized by match length |
| `kill_participation` | Share of team kills a player participated in |
| `visionScore` | Vision contribution during the match |


Current Limitations

This project is still in progress. Current limitations include:

- API key is currently stored directly in api.py
- Database schema may continue to change
- Some files are still experimental
- Analysis notebook and dashboard are not finalized
- Automated tests have not been added yet
- The collected sample may not perfectly represent the entire ranked player base
