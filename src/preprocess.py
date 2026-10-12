"""Starter preprocessing script for the student placement project.

Before running, set INPUT_FILE and TARGET_COLUMN to match your downloaded dataset.
This starter deliberately does not assume a particular dataset schema.
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

INPUT_FILE = ROOT / "data" / "raw" / "student_placement_raw_data.csv"
TARGET_COLUMN = "placement_status"



def main() -> None:
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found: {INPUT_FILE}. Put your downloaded CSV in data/raw/ "
            "and update INPUT_FILE in this script."
        )

    df = pd.read_csv(INPUT_FILE)
    print("Original shape:", df.shape)
    print("\nColumn names:", df.columns.tolist())
    print("\nMissing values by column:\n", df.isna().sum())
    print("\nDuplicate rows:", int(df.duplicated().sum()))

    # Conservative, transparent baseline cleaning:
    # 1. Remove exact duplicate rows.
    # 2. Do not automatically drop rows with missing values; inspect them first.
    cleaned = df.drop_duplicates().copy()

    # Save cleaned data. Dataset-specific imputation, outlier handling,
    # encoding and scaling should be added only after inspecting column types
    # and the dataset documentation.
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    cleaned.to_csv(OUTPUT_FILE, index=False)
    print("\nCleaned shape:", cleaned.shape)
    print("Saved:", OUTPUT_FILE)

    if TARGET_COLUMN in cleaned.columns:
        print(f"\nTarget distribution ({TARGET_COLUMN}):\n",
              cleaned[TARGET_COLUMN].value_counts(dropna=False))
    else:
        print(
            f"\nNote: target column '{TARGET_COLUMN}' was not found. "
            "Update TARGET_COLUMN after checking the dataset."
        )


if __name__ == "__main__":
    main()
