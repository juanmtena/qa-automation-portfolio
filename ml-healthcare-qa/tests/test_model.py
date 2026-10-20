import pandas as pd
import pytest

from src.data import FEATURES
from src.model import train_model


def test_minimum_quality(trained):
    _, metrics = trained
    assert metrics["r2"] >= 0.80
    assert metrics["mae"] <= 5.0


def test_predictions_in_valid_range(trained, df):
    model, _ = trained
    preds = model.predict(df[FEATURES])
    assert ((preds >= 0) & (preds <= 100)).all()


def test_training_is_deterministic(df):
    _, m1 = train_model(df, seed=1)
    _, m2 = train_model(df, seed=1)
    assert m1 == m2


def test_higher_previous_occupancy_increases_prediction(trained):
    model, _ = trained
    base = {"age_mean": 62, "day_of_week": 2, "month": 6, "flu_season": 0}
    low = pd.DataFrame([{**base, "prev_occupancy": 50}])[FEATURES]
    high = pd.DataFrame([{**base, "prev_occupancy": 90}])[FEATURES]
    assert model.predict(high)[0] > model.predict(low)[0]


@pytest.mark.parametrize("prev", [40, 95])
def test_boundary_inputs_do_not_break_model(trained, prev):
    model, _ = trained
    row = pd.DataFrame([{"age_mean": 30, "day_of_week": 6, "month": 12, "flu_season": 1, "prev_occupancy": prev}])[FEATURES]
    assert 0 <= model.predict(row)[0] <= 100
