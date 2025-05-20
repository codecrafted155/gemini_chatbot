import streamlit as st
import google.generativeai as genai


st.title("💬 Gemini Chatbot")

# Step 1: Fetch API key from environment variable (no need for user input in GUI)
api_key = "xyz"

# Step 2: Only proceed if API key is found
if api_key:
    try:
        # Step 3: Pass the API key to the genai SDK for authentication
        genai.configure(api_key="XYZ" )
            # Pass the API key here to configure the Gemini API

        # Step 4: Initialize the Gemini model after configuring the API
        model = genai.GenerativeModel('gemini-1.5-flash')

        # Step 5: Ask the user for input (what they want to ask the chatbot)
        user_input = st.text_input("Ask something:")

        # Step 6: If the user clicks the "Send" button and provides input, get a response from Gemini
        if st.button("Send") and user_input:
            response = model.generate_content(user_input)  # Generate content based on user input
            st.write("**Gemini:**", response.text)  # Show Gemini's response
    except Exception as e:
        st.error(f"Error: {str(e)}")  # Show error message if something goes wrong
else:
    st.warning("API Key not found. Please set the GEMINI_API_KEY environment variable.")  # Show warning if API key is not set



