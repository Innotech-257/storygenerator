import google.generativeai as genai
import streamlit as st
from gtts import gTTS
import os
import base64

# Function to generate audio from text
def text_to_speech( text ):
    tts = gTTS( text = text, lang = 'en' )
    tts.save( "story.mp3" )
    with open( "story.mp3", "rb" ) as audio_file:
        audio_bytes = audio_file.read()
    os.remove( "story.mp3" )
    return audio_bytes

# Function to create a download link for the audio
def get_audio_download_link( audio_bytes ):
    b64 = base64.b64encode( audio_bytes ).decode()
    return f'<a href="data:audio/mp3;base64,{b64}" download="story.mp3">Download Audio</a>'

# Streamlit app
st.title( "Story Generator" )

# Configure Gemini API
genai.configure( api_key = "AIzaSyA4O1-zyvh5PdWvQUt4hjTd1R5z6xI5A9w" )
model = genai.GenerativeModel( 'gemini-pro' )

# Story Generator
st.header( "Custom Story Generator" )
theme = st.selectbox( "Select a theme", [ "Fantasy", "Sci-Fi", "Romance", "Adventure", "Mystery", "Thriller" ] )
age_group = st.selectbox( "Select an age group", [ "Kids", "Tweens", "Teens", "Adults" ] )
time_of_day = st.selectbox( "Select a time period", [ "midnight", "morning", "noon", "afternoon", "evening", "night" ] )
length = st.slider( "Select the length of the story( in minutes )", 
                    min_value = 1.0, 
                    max_value = 30.0, 
                    value = 5.0,
                    step = 0.5 )

user_prompt = f"Tell me a {theme} story for {age_group}s that is {length} minutes long and takes place at {time_of_day}."

if st.button( "Generate Story" ):
    try:
        response = model.generate_content( user_prompt )
        story_text = response.text
        st.write( story_text )
        
        # Create columns for the story text and the audio button
        col1, col2 = st.columns( [ 0.9, 0.1 ] )
        
        with col1:
            st.write( story_text )
        
        with col2:
            audio_bytes = text_to_speech( story_text )
            st.audio( audio_bytes, format = 'audio/mp3' )
            st.markdown( get_audio_download_link( audio_bytes ), unsafe_allow_html = True )
        
    except Exception as e:
        st.error( f"Sorry, the story could not be generated: {str( e )}" )

