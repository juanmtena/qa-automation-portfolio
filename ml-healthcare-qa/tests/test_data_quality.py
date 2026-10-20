import pandas as pd

from src.data import COLUMNS, generate_synthetic_occupancy


def test_schema(df):
    assert list(df.columns) == COLUMNS


def test_no_nulls(df):
    assert not df.isnull().any().any()


def test_value_ranges(df):
    assert df["age_mean"].between(30, 90).all()
    assert df["day_of_week"].between(0, 6).all()
    assert df["month"].between(1, 12).all()
    assert df["flu_season"].isin([0, 1]).all()
    assert df["prev_occupancy"].between(0, 100).all()
    assert df["occupancy"].between(0, 100).all()


def test_flu_season_consistent_with_month(df):
    expected = df["month"].isin([11, 12, 1, 2]).astype(int)
    assert (df["flu_season"] == expected).all()


def test_generation_is_reproducible():
    pd.testing.assert_frame_equal(generate_synthetic_occupancy(seed=7), generate_synthetic_occupancy(seed=7))
