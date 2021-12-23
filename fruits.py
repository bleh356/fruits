import streamlit as st

# Section 1
import pandas as pd
st.write("FRUITS RECORD ON EXCEL")
files = ['https://github.com/datagy/mediumdata/raw/master/january.xlsx', 'https://github.com/datagy/mediumdata/raw/master/february.xlsx', 'https://github.com/datagy/mediumdata/raw/master/march.xlsx']
combined = pd.DataFrame()

# Section 2
for file in files:
  df = pd.read_excel(file, skiprows = 3)
  combined = combined.append(df, ignore_index = True)
  
# Section 3
combined.to_excel('combined.xlsx')
path = "C:\\combined.xlsx"
