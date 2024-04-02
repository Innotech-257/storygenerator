import streamlit as st
import google.generativeai as genai

genai.configure( api_key = "AIzaSyAZQ04kkEhkil29VeRgutZ9SY_XvgdqzFQ" )
generation_config = {
    "temperature" : 0.9,
    "top_p" : 1,
    "top_k" : 1,
    "max_output_tokens" : 2048,
}
safety_settings = [
    { "category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE" },
    { "category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE" },
    { "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE" },
    { "category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE" },
]

model = genai.GenerativeModel(
    model_name = "gemini-pro", generation_config = generation_config, safety_settings = safety_settings
)

st.title( "AI Story Generator" )

st.subheader( "What theme story do you want to listen to?" )
theme = st.multiselect("Theme:", ["scary", "funny", "night time", "adventure", "action", "interesting", "horror", "sci-fi", "thriller"])

st.subheader("What time of the day is it?")
time = st.multiselect(
    "Time of day:",
    ["morning - 6am - 12pm", "afternoon - 1pm - 5pm", "evening - 6pm - 8pm", "night - 9pm - 11pm", "late night - 12pm - 5am"],
)

st.subheader("How big is the audience?")
size = st.multiselect("Audience size:", ["1 person", "2 person", "3 person", "4 person", "more than 4 people"])

st.subheader("How long is the story?")
long = st.multiselect(
    "Story length:", ["1 - 2 min", "3 - 5 min", "6 - 8 min", "9 - 11 min", "more than 11 min"]
)

st.subheader( "age of the audience" )
age = st.multiselect( "Age:", [ "kids", "teens", "adults", "all ages"])

st.header("Press generate to generate your story")
generate = st.button("Generate")

if generate:
    prompt_parts = [ f"Create a story that is {long} and for {size} who are {age} the theme of the story is {theme} and the time of the day is {time}" ]
    response = model.generate_content(prompt_parts)

    st.text( response.text )
