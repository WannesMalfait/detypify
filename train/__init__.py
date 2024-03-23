import psycopg
from torch.utils.data import Dataset

from train.preprocess import *


class TypSamples(Dataset):
    def __init__(self):
        self.conn = psycopg.connect("dbname=detypify")
        self.len = self.conn.execute("SELECT COUNT(*) FROM typ_samples").fetchone()[0]

    def __len__(self):
        return self.len

    def __getitem__(self, idx):
        return self.conn.execute(
            """
            SELECT strokes, typ
            FROM typ_samples
            WHERE id = %s
            """,
            (idx + 1,),
        ).fetchone()


def main():
    preprocess()
