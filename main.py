import streamlit as st
import time

st.title('Streamlit 練習更新')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i +1)
    time.sleep(0.01)

'Done!!!!!'



# st.write(
#     pd.DataFrame({
#         '1st column': [1,2,3,4],
#         '2st column': [10,20,30,40]
#     })
# )

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



# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50]+[35.69, 139.70],
#     columns = [ 'lat', 'lon']
# )

# st.map(df)

# st.write('Display Image')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')


# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1,11))
# )
# 'あなたの好きな数字は、', option , 'です。'

# if st.checkbox('Show Image'):
#     img = Image.open('IMG_2198.JPG')
#     st.image(img, caption='こまち', use_column_width = True)

# st.write('Interactive Widgets')

# text = st.text_input('あなたの趣味を教えてください')
# st.write('あなたの趣味:', text)

# condition = st.slider('あなたの今の調子は', 0, 100, 50)
# st.write('あなたの調子は:', condition)