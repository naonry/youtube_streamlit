import streamlit as st
import time

import pandas as pd
import yfinance as yf
import altair as alt

st.title('可視化アプリ練習1')

st.sidebar.write("""
# GAFA株価
こちらは株価可視化ツールです。以下のオプションから表示日数を指定してください""")

st.sidebar.write("""
## 表示日数選択
# """)
days = st.sidebar.slider('日数', 1, 50, 20)

st.write(f"""
### 過去　**{days}日間** のGAFA株価
""")

@st.cache
def get_data(days, tickers):
    df = pd.DataFrame()
    for company in tickers.keys():
        tkr = yf.Ticker(tickers[company])
        hist = tkr.history(period=f'{days}d')
        hist.index = hist.index.strftime('%d %B %Y')
        hist = hist[['Close']]
        hist.columns = [company]
        hist = hist.T
        hist.index.name = 'Name'
        df = pd.concat([df, hist])
    return df

st.sidebar.write("""
## 株価の範囲指定
""")
ymin, ymax = st.sidebar.slider(
    '範囲を指定してください。',
    0.0, 3500.0, (0.0, 3500.0)
)

tickers = {
    'apple' : 'AAPL',
    'facebook' : 'FB',
    'google' : 'GOOGL',
    'microsoft' : 'MSFT',
    'netflix' : 'NFLX',
    'amazon' : 'AMZN'
}

df = get_data(days, tickers)
companies = st.multiselect(
    '会社名を選択してください。',
    list(df.index),
    ['google','amazon','facebook','apple']
)
try:
    if not companies:
        st.error('少なくとも一社は選んでください。')
    else:
        data = df.loc[companies]
        st.write("### 株価 (USD)", data.sort_index())
        data = data.T.reset_index()
        data = pd.melt(data, id_vars=['Date']).rename(
            columns={'value': 'Stock Prices(USD)'}
        )
        chart = (
            alt.Chart(data)
            .mark_line(opacity=0.8, clip=True)
            .encode(
                x="Date:T",
                y=alt.Y("Stock Prices(USD):Q", stack=None, scale=alt.Scale(domain=[ymin, ymax])),
                color='Name:N'
            )
        )
        st.altair_chart(chart, use_container_width=True)
except:
    st.error(
        "おっと！なにかエラーが起きているようです。"
    )
  



latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i +1)
    time.sleep(0.01)

'Done!!!!!'


"""
# レベル1 My 1st App
## レベル2
### レベル3
こんな感じでマジックコマンドを使用できる。Markdown対応

``` python
#pythonコードはこうしてかける
import streamlit as st
import pandas as pd
import numpy as np

```

``` R
library('brms')
```
"""

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

