import streamlit as st
import streamlit.components.v1 as components

st.title("Component tutorial")

_discrete_slider = components.declare_component(
    "discrete_slider", url="http://localhost:3001"
)


def discrete_slider(greetings, name="Streamlit", key=None):
    return _discrete_slider(greetings=greetings, name=name, default=0, key=key)


retrun_value = discrete_slider("Hi!", key="one")
st.write("Number of clicks", retrun_value)

retrun_value = discrete_slider("Hello!", key="two")
st.write("Number of clicks", retrun_value)
