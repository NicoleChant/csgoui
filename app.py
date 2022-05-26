import streamlit as st
import numpy as np

st.title("CSGO Predictions")
st.markdown("_If you don\'t know who I am, then maybe your best course would be to tread lightly_.")
st.markdown("~ Heisenberg")
st.caption("made by Nicole Chan")
st.image('images/csgo-media.jpg')


audio_file = open('csgoaudio.wav' , 'rb')
audio_bytes = audio_file.read()

with st.sidebar:
    st.markdown("Music Player")
    st.audio(audio_bytes , start_time = 0, format = 'audio/wav')
    st.sidebar.image('images/csgo_logo.png')

with st.expander("About"):
    st.write("""
      Welcome to CSGO Predictions. Lately e-sports have a massive boost in the betting industry.
      This app is designed to give you prediction of ongoing matches.""")

st.subheader("Model Features")
col1 , col2 = st.columns(2)

with col1:
    st.checkbox("Bomb has been planted")

with col2:
    with st.form(key = 'predict'):
        submitted = st.form_submit_button("Predict")

        if submitted:
            pass


st.subheader("Prediction")

st.bar_chart(np.random.randn(50,3))

st.image('images/csgo_snap.jpg')
