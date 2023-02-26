import streamlit as st

st.title(":red[innomatics] data app :sunglasses:")
st.snow()

btn_click = st.button("click Me!")

if btn_click == True:
    st.subheader("you clicked me :cry:")
    st.balloons()