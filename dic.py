import streamlit as st
import pandas as pd
import numpy as np
import graphviz as graphviz


st.title('Proto Dico Encyclopedica Arthuria')
df = pd.read_csv('dic_struct.csv')
concept = st.text_input('Enter a concept')
row = df.loc[df['Concepts'] == concept]
if concept:
    row = row.dropna(axis=1)
    row = row.values.tolist()
    st.write(row)



    #for i in row.iteritems():
    #    st.write(i)
else:
    st.write('rentrez un concept')


if st.button('Regarder le tableau en entier'):
    st.write(df)
else:
    st.write('cliquer pour montrer')