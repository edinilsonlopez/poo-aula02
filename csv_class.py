import pandas as pd

class csv_processor:
    def __init__(self,path:str):
        self.path = path
        self.df = None

    def load_csv(self):
        self.df = pd.read_csv(self.path)

    def filter_df(self, col:str,val:str):
        return self.df[self.df[col] == val]