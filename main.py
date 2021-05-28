import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time



st.title("Streamlit 超入門")

#プログレスバーの表示
st.write("プログレスバーの表示")
"Start!"
latest_iteration=st.empty()
bar=st.progress(0)
for i in range(100):
    latest_iteration.text(f"Iteration{i+1}")
    bar.progress(i+1)
    time.sleep(0.1)
"Done!!!"




#2カラムレイアウト
left_column,right_column=st.beta_columns(2)
button=left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

#エクスパンダー
expander=st.beta_expander("問い合わせ")
expander.write("問い合わせの回答")




#サイドバー
#text=st.sidebar.text_input("あなたの趣味を教えてください！")
#condition=st.sidebar.slider("あたなのいまの調子は？",0,100,50)
#"あなたの趣味：",text
#"コンディション：",condition

#ベース
#text=st.text_input("あなたの趣味を教えてください！！！")
#"あなたの趣味：",text
#condition=st.slider("あたなのいまの調子は？",0,100,50)
#"コンディション：",condition 

option=st.selectbox(
    "あなたが好きな数字を教えて下さい。",
    list(range(1,11))
)
"あなたの好きな数字は、",option,"です。"

st.write("Display Image")

if st.checkbox("rengoku Image"):
    img=Image.open("test.jpg")
    st.image(img,caption="rengokusan",use_column_width=True)



st.write("Date Frame")

df=pd.DataFrame({
    "1列目":[1,2,6,4],
    "2列目":[10,70,30,40]
})

df=pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=["lat","lon"])
df

st.map(df)

df=pd.DataFrame(
    np.random.rand(20,3),
    columns=["a","b","c"])
df

st.bar_chart(df) 

st.dataframe(df.style.highlight_max(axis=0),width=400,height =300)

st.table(df.style.highlight_max(axis=0))



"""
# 章
## 節
### 項
```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""