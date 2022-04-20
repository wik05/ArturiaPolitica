import streamlit as st
import pandas as pd
import numpy as np

st.title('Proto Dico Encyclopedica Arthuria')
df = pd.read_csv('dic_struct.csv')
concept = st.text_input('Enter a concept')
row = df.loc[df['Concepts'] == concept]
if concept:
    st.write(row)
else:
    st.write('rentrez un concept')


if st.button('Regarder le tableau en entier'):
    st.write(df)
else:
    st.write('cliquer pour montrer')