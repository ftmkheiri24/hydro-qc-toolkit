from __future__ import annotations

import argparse
from pathlib import Path

from io_utils import load_rainfall_excel, add_date_column
from summaries import monthly_totals, annual_totals, top_wettest_days
from qc import qc_summary, build_complete_daily
from report import make_qc_report_md


def main() -> int:
    parser = argparse.ArgumentParser(description="Daily rainfall QC + summaries")
    parser.add_argument("--infile", required=True, help="Path to input .xls/.xlsx file")
    parser.add_argument("--outdir", default="outputs", help="Output folder")
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    df = load_rainfall_excel(args.infile)
    df = add_date_column(df)

    # Summaries
    monthly = monthly_totals(df)
    annual = annual_totals(df)
    top10 = top_wettest_days(df, n=10)

    monthly.to_csv(outdir / "monthly_totals.csv", index=False)
    annual.to_csv(outdir / "annual_totals.csv", index=False)
    top10.to_csv(outdir / "top10_wettest_days.csv", index=False)

    # QC + complete daily series
    stats = qc_summary(df)
    complete = build_complete_daily(df)
    complete.to_csv(outdir / "complete_daily.csv", index=False)

    report_md = make_qc_report_md(stats)
    (outdir / "qc_report.md").write_text(report_md, encoding="utf-8")

    print("Saved:", outdir / "monthly_totals.csv")
    print("Saved:", outdir / "annual_totals.csv")
    print("Saved:", outdir / "top10_wettest_days.csv")
    print("Saved:", outdir / "complete_daily.csv")
    print("Saved:", outdir / "qc_report.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())