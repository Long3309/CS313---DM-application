import streamlit as st 
import pandas as pd
data = pd.read_csv(r"datasets\movie_metadata.csv")
st.dataframe(data)
code = '''
data.isnull().sum()
col = data["duration"]
col = col.dropna()
zscore = stats.zscore(col)
res = np.where(zscore > 3.0)
res
'''
st.code(code, language= "python")
