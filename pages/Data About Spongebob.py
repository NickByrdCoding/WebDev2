import streamlit as st
#import json
infile = open("spongebobdata.json")

st.header("Data About Me!")
#spongeData = json.load(infile)
spongeData = [{
  "Weekly Task": ["Reading", "Jellyfishing", "Blowing Bubbles", "Singing", "Working"],
  "Hours Attempted": [5, 6, 4, 5, 3]
},

{
  "Season": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
  "Episodes": [20, 20, 20, 20, 20, 26, 26, 26, 26, 11, 26, 25, 26]
},

{
  "Months": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
  "Searches": [63, 62, 63, 68, 68, 92, 71, 63, 60, 54, 53, 55]
},
{
    "Months": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    "Searches": [54, 53, 57, 58, 59, 57, 56, 52, 50, 50, 53, 52]
  },
{
    "Months": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    "Searches": [56, 54, 55, 59, 61, 57, 62, 56, 52, 57, 54, 57]
  },
{
    "Months": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    "Searches": [61, 61, 57, 58, 58, 59, 60, 59, 56, 57, 51, 52]
  },
{
    "Months": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    "Searches": [55, 65, 59, 60, 62, 59, 60, 64, 63, 74, 60, 60]
  }
]

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
