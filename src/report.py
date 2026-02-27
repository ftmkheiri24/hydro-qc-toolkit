from __future__ import annotations

from typing import Any, Dict


def make_qc_report_md(stats: Dict[str, Any]) -> str:
    date_min = stats["date_min"].date() if stats["date_min"] is not None else "N/A"
    date_max = stats["date_max"].date() if stats["date_max"] is not None else "N/A"

    max_date = stats["max_daily_rain_date"]
    max_date_str = max_date.date() if max_date is not None else "N/A"

    lines = []
    lines.append("# QC Report — Daily Rainfall\n\n")
    lines.append(f"- Date range: **{date_min}** to **{date_max}**\n")
    lines.append(f"- Rows: **{stats['n_rows']}**\n")
    lines.append(f"- Unique days in file: **{stats['unique_days_in_file']}**\n")
    lines.append(f"- Expected days in range: **{stats['expected_days_in_range']}**\n")
    lines.append(f"- Days without records in file: **{stats['days_without_records_in_file']}**\n\n")

    lines.append("## Data checks\n")
    lines.append(f"- Missing rain values: **{stats['missing_rain_values']}**\n")
    lines.append(f"- Negative rain values: **{stats['negative_rain_values']}**\n")
    lines.append(f"- Duplicate calendar days: **{stats['duplicate_days']}**\n\n")

    lines.append("## Basic stats\n")
    if stats["max_daily_rain_in"] is None:
        lines.append("- Max daily rainfall: N/A\n")
    else:
        lines.append(f"- Max daily rainfall: **{stats['max_daily_rain_in']:.3f} in** on **{max_date_str}**\n")

    lines.append("\n## Notes\n")
    lines.append("- `days_without_records_in_file` means dates not present in the source file (could be dry days or unreported days).\n")
    lines.append("- `complete_daily.csv` fills missing dates with 0 and adds `record_present` for transparency.\n")

    return "".join(lines)
