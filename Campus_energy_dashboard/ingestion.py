from pathlib import Path
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def read_all_csvs(data_dir="data"):
    data_dir = Path(data_dir)
    files = list(data_dir.glob("*.csv"))
    frames = []
    bad_files = []

    if not files:
        logger.warning("No CSV files found inside /data folder.")

    for f in files:
        try:
            df = pd.read_csv(f, parse_dates=['timestamp'], on_bad_lines='skip')

            if 'kwh' not in df.columns:
                logger.warning(f"{f.name} missing 'kwh' column. Skipping.")
                bad_files.append(f.name)
                continue

            if 'building' not in df.columns:
                building_name = f.stem.split("_")[0]
                df['building'] = building_name

            frames.append(df)

        except Exception as e:
            logger.warning(f"Error reading {f.name}: {e}")
            bad_files.append(f.name)

    if frames:
        df_all = pd.concat(frames, ignore_index=True)
        df_all = df_all.sort_values("timestamp")
        return df_all, bad_files

    return pd.DataFrame(), bad_files
