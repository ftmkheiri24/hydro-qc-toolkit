# Hydro QC Toolkit (Daily Rainfall)

A small Python tool for quality checks (QC) and summary statistics on daily rainfall time series.
It reads a station rainfall file (Excel), builds a clean `date` column, and exports ready-to-use outputs (CSV + a QC report).

## Features
- Load daily rainfall data from Excel (`.xls/.xlsx`)
- Build a proper daily `date` column from `year/month/day`
- QC checks:
  - missing rainfall values
  - negative rainfall values
  - duplicate calendar days
  - days without records in the file (within the full date range)
- Summary outputs:
  - monthly totals
  - annual totals
  - top 10 wettest days
- Standardized daily series:
  - `complete_daily.csv` (fills missing dates with 0 and adds `record_present`)

## Input format
The input file is expected to have 7 columns (in this order):
- `station`, `water_year`, `year`, `month`, `day`, `rain_in`, `flag`

Note: The source file may not contain a complete daily record.  
The tool reports days without records and creates `complete_daily.csv` with a `record_present` flag for transparency.

## Installation
```bash
pip install -r requirements.txt

Last updated: 2026-02-28T00:23:15+03:30
