"""Datos SINTÉTICOS de ocupación hospitalaria. No contiene datos reales de pacientes."""
import numpy as np
import pandas as pd

COLUMNS = ["age_mean", "day_of_week", "month", "flu_season", "prev_occupancy", "occupancy"]
FEATURES = COLUMNS[:-1]
TARGET = "occupancy"


def generate_synthetic_occupancy(n: int = 1000, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    df = pd.DataFrame(
        {
            "age_mean": rng.normal(62, 6, n).clip(30, 90).round(1),
            "day_of_week": rng.integers(0, 7, n),
            "month": rng.integers(1, 13, n),
            "prev_occupancy": rng.uniform(40, 95, n).round(1),
        }
    )
    df["flu_season"] = df["month"].isin([11, 12, 1, 2]).astype(int)
    occupancy = (
        15
        + 0.75 * df["prev_occupancy"]
        + 8 * df["flu_season"]
        - 3 * (df["day_of_week"] >= 5)
        + 0.1 * (df["age_mean"] - 62)
        + rng.normal(0, 2, n)
    )
    df[TARGET] = occupancy.clip(0, 100).round(1)
    return df[COLUMNS]
