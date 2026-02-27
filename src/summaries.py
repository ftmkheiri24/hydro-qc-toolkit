from __future__ import annotations

import pandas as pd


def monthly_totals(df: pd.DataFrame) -> pd.DataFrame:
    out = (
        df.groupby(["year", "month"], as_index=False)["rain_in"]
        .sum()
        .rename(columns={"rain_in": "total_rain_in"})
    )
    return out


def annual_totals(df: pd.DataFrame) -> pd.DataFrame:
    out = (
        df.groupby("year", as_index=False)["rain_in"]
        .sum()
        .rename(columns={"rain_in": "total_rain_in"})
    )
    return out


def top_wettest_days(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    out = df[["date", "rain_in"]].dropna().sort_values("rain_in", ascending=False).head(n)
    return out.reset_index(drop=True)