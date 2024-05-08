import pandas as pd

# 1. Baca dataset
print("[1] BACA DATASET")
df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_test.csv', low_memory=False)
print("    Dataset:\n", df.head())
print("    Info:\n", df.info())

# 2. Ubah tipe data
print("\n[2] UBAH TIPE DATA")
df["customer_id"] = df["customer_id"].apply(lambda x: x.split("'")[1]).astype('int64')
df["quantity"] = df["quantity"].apply(lambda x: x.split("'")[1]).astype('int64')
df["item_price"] = df["item_price"].apply(lambda x: x.split("'")[1]).astype('int64')
print("    Tipe data:\n", df.dtypes)

# 3. Transform "product_value" supaya bentuknya seragam dengan format "PXXXX", assign ke kolom baru "product_id", dan drop kolom "product_value", jika terdapat nan gantilah dengan "unknown"
print("\n[3] TRANSFORM product_value MENJADI product_id")
# Buat fungsi
import math
def impute_product_value(val):
    if math.isnan(val):
        return 'unknown'
    else:
        return 'P' + '{:0>4}'.format(str(val).split('.')[0])
# Buat kolom "product_id"
df["product_id"] = df["product_value"].apply(lambda x: impute_product_value(x))
# Hapus kolom "product_value"
df.drop(['product_value'], axis=1, inplace=True)
# Cetak 5 data teratas
print(df.head())