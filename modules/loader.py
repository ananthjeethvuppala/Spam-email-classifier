import pandas as pd

def load_dataset(file_path):

    data = pd.read_csv(
        file_path,
        encoding="latin-1"
    )

    data = data[['v1', 'v2']]
    data.columns = ['label', 'message']
    
    return data