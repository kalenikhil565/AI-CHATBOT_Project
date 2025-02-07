import streamlit as st
from transformers import pipeline

# Load chatbot model
chatbot = pipeline("text-generation", model="distilgpt2")

def healthcare_chatbot(user_input):
    user_input = user_input.lower()
    
    if "symptom" in user_input:
        return "Please consult a doctor for accurate advice."
    elif "appointment" in user_input:
        return "Would you like to schedule an appointment with the doctor?"
    elif "medication" in user_input:
        return "It's important to take prescribed medicines regularly. If you have concerns, consult your doctor."
    else:
        response = chatbot(user_input, max_length=50, num_return_sequences=1)
        return response[0]['generated_text']

def main():
    st.title("Healthcare Assistant Chatbot")
    
    user_input = st.text_input("How can I assist you today?", key="input")
    
    if st.button("Submit"):
        if user_input.strip():
            st.write("User:", user_input)
            with st.spinner("Processing your query, please wait..."):
                response = healthcare_chatbot(user_input)
                st.write("Healthcare Assistant:", response)
        else:
            st.warning("Please enter a message to get a response.")

if __name__ == "__main__":
    main()
