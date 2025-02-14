import streamlit as st
import json
infile = open("data/spongebobdata.json")

st.header("Data About Me!")
spongeData = json.load(infile)

if "data" not in st.session_state:
    st.session_state["data"] = spongeData



tab1, tab2, tab3 = st.tabs(["About Spongebob", "About the Show", "Viewership Over Time"])


with tab1:
  st.button(label = "Update Chart", key="Update1")
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

with tab3:
  year = st.select_slider(
    "Which year would you like to see?",
    options=[
        "2020",
        "2021",
        "2022",
        "2023",
        "2024",
    ],
)
  st.subheader(f"Viewership in: {year}")
  if year == "2020":
    st.line_chart(data = st.session_state["data"][2], x = "Months", y = "Searches", width=500, height=500)
  if year == "2021":
    st.line_chart(data = st.session_state["data"][3], x = "Months", y = "Searches", width=500, height=500)
  elif year == "2022":
    st.line_chart(data = st.session_state["data"][4], x = "Months", y = "Searches", width=500, height=500)
  elif year == "2023":
    st.line_chart(data = st.session_state["data"][5], x = "Months", y = "Searches", width=500, height=500)
  elif year == "2024":
    st.line_chart(data = st.session_state["data"][6], x = "Months", y = "Searches", width=500, height=500)
