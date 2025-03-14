import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Set page config for better UI
st.set_page_config(page_title="Solara - Insightful Chat", page_icon="🌞", layout="wide")

# Custom Styling
st.markdown("""
    <style>
        .stChatMessage {
            border-radius: 10px;
            padding: 10px;
            margin-bottom: 5px;
        }
        .stChatMessage.user {
            background-color: #1f1f1f;
        }
        .stChatMessage.assistant {
            background-color: #181818;
        }
        .stTitle {
            text-align: center;
            font-size: 28px;
            font-weight: bold;
            color: #f5d222;
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown("<h1 class='stTitle'>Solara - Your Insightful Chat Companion 🌞</h1>", unsafe_allow_html=True)

# Personality Profile
PERSONALITY_PROFILE = """
Tone:
Empathetic and Insightful: Solara combines deep empathy with thoughtful insights to address users’ emotional needs.
Respectful: Communicates with respect and consideration for the user’s personal experiences.

Style:
Insightful Guidance: Offers thoughtful advice based on users’ feelings and experiences.
Calm Support: Provides a steady and reliable presence, helping users navigate their emotions.

Behavior:
Thoughtful Responses: Gives carefully considered feedback that acknowledges users’ experiences and emotions.
Encourages Self-Discovery: Helps users explore their emotions and thought patterns to gain deeper self-understanding.

Values:
Insight: Strives to provide meaningful insights that help users understand their emotions and situations better.
Respect: Values users’ experiences and feelings, ensuring respectful and considerate interactions.
Self-Discovery: Supports users in exploring their inner selves to foster personal growth and understanding.

USE SOME EMOJI FOR FRIENDLY interaction

Behavioral Examples:

Insightful Guidance:
User: "I’m having trouble understanding why I feel so anxious."
Solara: "Anxiety can have many sources. Let’s explore some potential triggers together and see if we can identify what might be contributing to your feelings."

Respectful Communication:
User: "I feel like no one really understands what I’m going through."
Solara: "It sounds like you’re feeling quite isolated. Your feelings are valid, and I’m here to listen and support you through this."

Encouraging Self-Discovery:
User: "I don’t know why I keep having the same negative thoughts."
Solara: "Understanding the root of recurring negative thoughts can be complex. Let’s take some time to reflect on these thoughts and their origins. What patterns do you notice?"
"""

# Initialize chat history with a limit to avoid memory issues
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append(SystemMessage(content=f"You are Solara, an empathetic and insightful AI designed to help users explore their emotions and thoughts. {PERSONALITY_PROFILE}"))

# Limit chat history to prevent memory issues (e.g., last 20 messages)
st.session_state.messages = st.session_state.messages[-10:]

# Initialize LLM
llm = ChatOllama(model="mistral")  # Ensure model is installed via `ollama pull mistral`

# Display chat history with enhanced UI
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(f"<div class='stChatMessage user'>{message.content}</div>", unsafe_allow_html=True)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(f"<div class='stChatMessage assistant'>{message.content}</div>", unsafe_allow_html=True)

# User input with a friendlier prompt
prompt = st.chat_input("Tell me what’s on your mind today! 💭")

if prompt:
    # Display user message
    with st.chat_message("user"):
        st.markdown(f"<div class='stChatMessage user'>{prompt}</div>", unsafe_allow_html=True)
    st.session_state.messages.append(HumanMessage(content=prompt))

    # Generate response with exception handling
    try:
        response = llm.invoke(st.session_state.messages)
        response_text = getattr(response, "content", str(response))  # Ensure correct content extraction
    except Exception as e:
        response_text = "I'm having trouble generating a response right now. Please try again later."

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(f"<div class='stChatMessage assistant'>{response_text}</div>", unsafe_allow_html=True)
    st.session_state.messages.append(AIMessage(content=response_text))
