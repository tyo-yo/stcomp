import streamlit as st
import streamlit.components.v1 as components

st.title("Component tutorial")

_my_component = components.declare_component(
    "my_component", url="http://localhost:3001"
)


def my_component(greetings, name="Streamlit", key=None):
    return _my_component(greetings=greetings, name=name, default=0, key=key)


retrun_value = my_component("Hi!", key="one")
st.write("Number of clicks", retrun_value)

retrun_value = my_component("Hello!", key="two")
st.write("Number of clicks", retrun_value)
