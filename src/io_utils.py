from __future__ import annotations

import pandas as pd


EXPECTED_COLS = ["station", "water_year", "year", "month", "day", "rain_in", "flag"]


def load_rainfall_excel(path: str) -> pd.DataFrame:
    df = pd.read_excel(path)

    if df.shape[1] < 7:
        raise ValueError(f"Expected at least 7 columns, got {df.shape[1]}")

    df = df.iloc[:, :7].copy()
    df.columns = EXPECTED_COLS
    return df


def add_date_column(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["date"] = pd.to_datetime(df[["year", "month", "day"]], errors="coerce")
    df = df.dropna(subset=["date"]).sort_values("date").reset_index(drop=True)

    df["rain_in"] = pd.to_numeric(df["rain_in"], errors="coerce")
    df["date"] = df["date"].dt.normalize()
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    return df
