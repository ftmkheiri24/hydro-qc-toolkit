from __future__ import annotations

import pandas as pd


def qc_summary(df: pd.DataFrame) -> dict:
    n_rows = len(df)
    date_min = df["date"].min()
    date_max = df["date"].max()

    missing_rain = int(df["rain_in"].isna().sum())
    negative_rain = int((df["rain_in"] < 0).sum())

    dup_counts = df.groupby("date").size()
    dup_days = dup_counts[dup_counts > 1]
    n_duplicate_days = int(len(dup_days))

    expected_days = int((date_max - date_min).days) + 1
    present_days = int(df["date"].nunique())
    days_without_records = expected_days - present_days

    max_rain = df["rain_in"].max(skipna=True)
    max_day = None
    if pd.notna(max_rain):
        max_day = df.loc[df["rain_in"].idxmax(), "date"]

    return {
        "n_rows": n_rows,
        "date_min": date_min,
        "date_max": date_max,
        "missing_rain_values": missing_rain,
        "negative_rain_values": negative_rain,
        "duplicate_days": n_duplicate_days,
        "expected_days_in_range": expected_days,
        "unique_days_in_file": present_days,
        "days_without_records_in_file": days_without_records,
        "max_daily_rain_in": float(max_rain) if pd.notna(max_rain) else None,
        "max_daily_rain_date": max_day,
    }


def build_complete_daily(df: pd.DataFrame) -> pd.DataFrame:
    daily = df.groupby("date", as_index=False)["rain_in"].sum()

    full_index = pd.date_range(daily["date"].min(), daily["date"].max(), freq="D")
    complete = (
        daily.set_index("date")
        .reindex(full_index)
        .rename_axis("date")
        .reset_index()
    )

    complete["record_present"] = complete["rain_in"].notna()
    complete["rain_in"] = complete["rain_in"].fillna(0.0)
    return complete