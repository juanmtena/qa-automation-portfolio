from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

from src.data import FEATURES, TARGET


def train_model(df, seed: int = 42):
    x_train, x_test, y_train, y_test = train_test_split(df[FEATURES], df[TARGET], test_size=0.2, random_state=seed)
    model = RandomForestRegressor(n_estimators=100, random_state=seed).fit(x_train, y_train)
    pred = model.predict(x_test)
    return model, {"r2": r2_score(y_test, pred), "mae": mean_absolute_error(y_test, pred)}
