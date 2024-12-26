import streamlit as st
import re

st.markdown("<h1 style='text-align: center'>Density Checker</h1>", unsafe_allow_html=True)
st.markdown("---")


words_dict = dict()
text = st.text_area("Paragraph")
col1, col2, col3 = st.columns(3)
if text:
    sim_text = re.sub("[.?!&*;:,]", "", text)
    words = sim_text.lower().split(" ")
    for word in words:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
            
    keys = list(words_dict.keys())
    value = list(words_dict.values())
    for i in range(len(keys)):
        col1.markdown(f"<h5>{keys[i]}</h5>", unsafe_allow_html=True)
        col2.markdown(f"<h5>{value[i]}</h5>", unsafe_allow_html=True)
        col3.markdown(f"<h5>{round((value[i]/len(words)) * 100)}%</h5>", unsafe_allow_html=True)