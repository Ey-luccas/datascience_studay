#import pandas as pd
from bibliotecas import pd
adult_data = r"C:\Users\eyluc\Documents\ESTUDO -- 'data scientist'\Eydatascience\Estudos\Datasets\datasets_not_csv\adult.data"
columns = [
    "age", "workclass", "fnlwgt", "education", "education_num",
    "marital_status", "occupation", "relationship", "race",
    "sex", "capital_gain", "capital_loss", "hours_per_week",
    "native_country", "income"
]
data = pd.read_csv(adult_data, header=None, names=columns, skipinitialspace=True)
csv_output_path = r"C:\Users\eyluc\Documents\ESTUDO -- 'data scientist'\Eydatascience\Estudos\Datasets\csv\adult.csv"
data.to_csv(csv_output_path, index=False)
