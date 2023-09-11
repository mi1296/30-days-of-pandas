import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    return scores.sort_values(
        by='score', ascending=False,
    ).assign(
        rank=scores['score'].rank(method='dense', ascending=False),
    )[['score', 'rank']]
