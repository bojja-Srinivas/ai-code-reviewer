import streamlit as st
import google.generativeai as ai
st.title("_Welcome to AI Code Reviewer Application_ :sunglasses:")
user_prompt = st.text_area("Enter the code:", placeholder="Type your code here...")
btn_click = st.button("Review code")

# Read the API key from a file
with open("Google api key.txt") as f:
    key = f.read()

# Configure the AI model
ai.configure(api_key=key)
sys_prompt = """You are a helpful code reviewer application. Students will ask you to review and debug their code. 
Code Review
Bug Report: 
List any occurring errors. 
Fixed Code: 
Provide the corrected version of the entered code. 
make sure "Code Review" is the main heading and "Bug Report" and "Fixed Code" are subtitles, with "Code Review" as a bold title .
You are expected to reply in as much detail as possible. If a student asks a question outside the scope of code review, politely decline and ask them to focus on code review-related queries only."""
model = ai.GenerativeModel(model_name="models/gemini-1.5-flash", system_instruction=sys_prompt)

if btn_click:
    response = model.generate_content(user_prompt)
    st.write(response.text)
