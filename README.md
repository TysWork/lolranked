# League of Legends Match Data Pipeline (WIP)

## Overview
This repository contains a **work-in-progress data ingestion pipeline** built around the Riot Games League of Legends API.  
The project focuses on collecting ranked match data, storing it in a structured database, and preparing it for downstream analysis.

The emphasis is on **data engineering fundamentals**: API interaction, rate limiting, structured storage, and incremental development.

---

## Current Functionality
At its current stage, the pipeline supports:

- Retrieving ranked player identifiers (PUUIDs)
- Collecting match IDs for individual players
- Fetching detailed match-level data from the Riot API
- Persisting match and participant data to a local database
- Logging progress and handling API rate limits during long runs

The system is designed to scale gradually from single-player testing to larger ranked datasets.

---

## Project Structure
league/

│

├── api.py # Riot API requests and rate limiting

├── collect_details.py # Match detail collection logic

├── main.py # Pipeline entry point

├── database/ # Database initialization and helpers

├── analysis/ # (Planned) analysis scripts / notebooks

└── README.md

File organization may evolve as the project matures.

---

## Technologies Used

- Python
- Riot Games API
- SQLite
- pandas
- requests

---

## Motivation
This project was built to gain hands-on experience with:

- Real-world API constraints and pagination
- Designing repeatable data ingestion workflows
- Structuring semi-structured data for relational storage
- Building datasets suitable for SQL-based analysis

The project is intentionally backend-focused rather than visualization-first.

---

## Known Limitations
Because this project is under active development:

- Database schema is subject to change
- Error handling is incomplete for some edge cases
- No automated tests are implemented yet
- Analysis and visualization are not finalized

These limitations are acknowledged and planned for.

---

## Planned Improvements
- Normalize database schema (players, matches, participants)
- Add SQL-based analysis queries
- Create exploratory analysis notebooks
- Introduce basic automated testing
- Improve documentation and reproducibility

---

## Running the Project
This project is currently intended for local development and experimentation.

```bash
python main.py
