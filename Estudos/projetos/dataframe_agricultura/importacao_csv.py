from datasets import load_dataset
import pandas as pd

dataset = load_dataset("Solshine/Reflection-Tuning-Natural-Farming_Agricultural-Dataset")

df_train = dataset['train'].to_pandas()

print(df_train.head())