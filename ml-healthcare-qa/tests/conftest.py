import pytest

from src.data import generate_synthetic_occupancy
from src.model import train_model


@pytest.fixture(scope="session")
def df():
    return generate_synthetic_occupancy()


@pytest.fixture(scope="session")
def trained(df):
    return train_model(df)
