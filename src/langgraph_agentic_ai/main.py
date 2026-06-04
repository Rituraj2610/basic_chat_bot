import streamlit as st

from src.langgraph_agentic_ai.ui.streamlit.loadui import LoadStreamlitUI

def load_langgraph_agentic_ai_app():
    """
    Loads and runs the Langgraph Agentic AI APplication with Streamlit UI.
    This function initializes the ui, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while
    implementing exception handling for robustness
    """

    # LOAD UI

    ui = LoadStreamlitUI()  # class
    user_input = ui.load_streamlit_ui() # class's method

    if not user_input:
        st.error("Failed to load user input")
        return

    user_message = st.chat_input("Enter your message")

