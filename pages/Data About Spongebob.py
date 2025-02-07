import streamlit as st
import json
infile = open("spongebobdata.json")

st.header("Data About Me!")
spongeData = json.load(infile)

if "data" not in st.session_state:
    st.session_state["data"] = spongeData



tab1, tab2 = st.tabs(["About Spongebob", "About the Show"])


with tab1:
  st.button("Update Chart")
  st.bar_chart(data = st.session_state["data"][0], x = "Weekly Task", y = "Hours Attempted")
  task = st.selectbox("Which task would you like to update?", ("None", "Blowing Bubbles", "Jellyfishing", "Reading", "Singing", "Working"))
  if task == "Blowing Bubbles":
    bubbles = st.slider("Blowing Bubbles: ", 0, 30, st.session_state["data"][0]["Hours Attempted"][2])
    st.session_state["data"][0]["Hours Attempted"][2] = bubbles
  elif task == "Jellyfishing":
    jellyfishing = st.slider("Jellyfishing", 0, 30, st.session_state["data"][0]["Hours Attempted"][1])
    st.session_state["data"][0]["Hours Attempted"][1] = jellyfishing
  elif task == "Reading":
    reading = st.slider("Reading: ", 0, 30, st.session_state["data"][0]["Hours Attempted"][0])
    st.session_state["data"][0]["Hours Attempted"][0] = reading
  elif task == "Singing":
    singing = st.slider("Singing", 0, 30, st.session_state["data"][0]["Hours Attempted"][3])
    st.session_state["data"][0]["Hours Attempted"][3] = singing
  elif task == "Working":
    working = st.slider("Working", 0, 30, st.session_state["data"][0]["Hours Attempted"][4])
    st.session_state["data"][0]["Hours Attempted"][4] = working


with tab2:
  st.line_chart(data = spongeData[1], x = "Season", y = "Episodes")
  st.subheader("Episodes Per Season: ")
  st.caption("The line graph displays the number of SpongeBob SquarePants episodes per season. The x-axis represents the season numbers (from 1 to the latest season), while the y-axis indicates the number of episodes produced in each season. Season 1 came out in 1999 and season 13 came out in 2023")