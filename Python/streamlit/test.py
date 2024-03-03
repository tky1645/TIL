import pandas as pd
import time

import gspread
import pandas as pd
from google.oauth2 import service_account
import operateSheet

question_categories = ["日付", "カテゴリ", "詳細", "収入", "支出"]

# スプレッドシートの認証
scopes = [ 'https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'
]
import toml
with open('./secrets.toml') as f:
    secrets = toml.load(f)

credentials = service_account.Credentials.from_service_account_info( secrets["gcp_service_account"], scopes=scopes
)
gc = gspread.authorize(credentials)
# スプレッドシートからデータ取得
SP_SHEET_KEY = secrets["SP_SHEET_KEY"]["key"] # スプレッドシートのキー
sh = gc.open_by_key(SP_SHEET_KEY)
SP_SHEET = 'シート1' # シート名「シート1」を指定
worksheet = sh.worksheet(SP_SHEET)
target_row = 1
worksheet = sh.worksheet(SP_SHEET)
data_to_write = [[value] for value in question_categories]
operateSheet.copyDataToBudgetSheet(data_to_write, worksheet)
data = worksheet.get_all_values() # シート内の全データを取得
df = pd.DataFrame(data[1:], columns=data[0]) # 取得したデータをデータフレームに変換
print(df)


date = "2023/10/02"
category = "給料"
description = "メモ"
income = 1000
expense = 0

val = date
questions = [val, category, description, income, expense]
result = [[category, answer] for category, answer in zip(question_categories, questions)]

operateSheet.copyDataToBudgetSheet(result, worksheet, True)

data = worksheet.get_all_values() # シート内の全データを取得
df = pd.DataFrame(data[1:], columns=data[0]) # 取得したデータをデータフレームに変換
print(df)
df["収入"] = df["収入"].replace('', '0').astype(int)
df["支出"] =df["支出"].replace('', '0').astype(int)

# 日付列を日付型に変換
df['日付'] = pd.to_datetime(df['日付'], format='ISO8601')

# 月別カテゴリー別棒グラフを作りたい

df['月'] = df['日付'].dt.strftime('%Y-%m')
df['収支'] = df['収入'] - df['支出']
pivot_df = df.pivot_table(index='月', columns='カテゴリ', values='収支', aggfunc='sum', fill_value=0).reset_index()
#cat_monthly_summary = df.groupby(['月', 'カテゴリ'])['支出'].sum().reset_index()

print(pivot_df)

# 月別合計収支を作りたい
monthly_total = pivot_df.groupby('月').sum()

# 合計列を追加
monthly_total['合計'] = monthly_total.sum(axis=1)
print(monthly_total)

#melt
#loc


# 月ごとにグループ化し、収支を合計
monthly_summary = df.groupby('月')['支出'].sum().reset_index()

# 新しいDataFrameに結果を格納
print(monthly_summary)