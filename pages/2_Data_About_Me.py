import streamlit as st
import json
infile = open("spongebobdata.json")

st.header("Data About Me!")
spongeData = json.load(infile)

if "data" not in st.session_state:
    st.session_state["data"] = spongeData



tab1, tab2, tab3 = st.tabs(["About the Show", "About Spongebob", "Viewership Over Time"])


with tab2:
  st.caption("Everytime you press a button Streamlit reruns the code below the button, causing the graph data to update!")
  st.button(label = "Update Chart", key="Update1")
  st.bar_chart(data = st.session_state["data"][0], x = "Weekly Task", y = "Hours Attempted")
  st.caption("This is a **dynamic** graph as it can be changed by user input. This graph displays data from a **.json()** file^")
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
  st.caption("Due to saving data into **st.session_state**, Streamlit remembers previous changes made to the graph even when updated again! If the data wasn't stored in **st.session_state**, updating the chart would cause previous changes to be reset.")

with tab1:
  st.line_chart(data = spongeData[1], x = "Season", y = "Episodes")
  st.caption("This is a **static** line graph that displays data from a **.json()** file^")
  st.subheader("Episodes Per Season: ")
  st.write("The line graph displays the number of SpongeBob SquarePants episodes per season. The x-axis represents the season numbers (from 1 to the latest season), while the y-axis indicates the number of episodes produced in each season. Season 1 came out in 1999 and Season 13 came out in 2023.")

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
  st.caption("This is a **dynamic** graph as it can be changed by user input. This graph displays data from a **.json()** file ^")

