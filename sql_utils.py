import pandas as pd

def fetch2frame(cursor):
    """Fetch all items from `cursor` and return a DataFrame."""
    columns = [x[0] for x in cursor.description]
    return pd.DataFrame(cursor.fetchall(), columns=columns)