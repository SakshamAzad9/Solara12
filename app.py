import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from context_engine import ContextEngine
from ui_components import UIComponents
from personality import PersonalityManager
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SolaraApp:
    def __init__(self):
        self.ui = UIComponents()
        self.personality = PersonalityManager()
        self.context_engine = ContextEngine()
        self.llm = None
        self.initialize_app()
    
    def initialize_app(self):
        """Initialize the Streamlit app configuration and components"""
        st.set_page_config(
            page_title="Solara - Insightful Chat",
            page_icon="🌞",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        
        # Apply custom styling
        self.ui.apply_custom_styling()
        
        # Initialize session state
        self.initialize_session_state()
        
        # Initialize LLM
        self.initialize_llm()
    
    def initialize_session_state(self):
        """Initialize session state variables"""
        if "messages" not in st.session_state:
            st.session_state.messages = []
            # Add system message with enhanced context
            system_prompt = self.personality.get_enhanced_system_prompt()
            st.session_state.messages.append(SystemMessage(content=system_prompt))
        
        if "conversation_context" not in st.session_state:
            st.session_state.conversation_context = {
                "user_emotions": [],
                "topics_discussed": [],
                "session_start": datetime.now().isoformat(),
                "interaction_count": 0
            }
        
        if "user_profile" not in st.session_state:
            st.session_state.user_profile = {
                "name": None,
                "preferred_communication_style": "balanced",
                "emotional_state": "neutral"
            }
    
    def initialize_llm(self):
        """Initialize the language model with error handling"""
        try:
            self.llm = ChatOllama(
                model="mistral",
                temperature=0.7,
                top_p=0.9
            )
            logger.info("LLM initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize LLM: {e}")
            st.error("Failed to initialize the AI model. Please check your Ollama installation.")
    
    def render_sidebar(self):
        """Render the sidebar with controls and context information"""
        with st.sidebar:
            st.title("🌞 Solara Settings")
            
            # User Profile Section
            st.subheader("👤 Your Profile")
            user_name = st.text_input("Your Name (Optional)", 
                                    value=st.session_state.user_profile.get("name", ""))
            if user_name != st.session_state.user_profile.get("name"):
                st.session_state.user_profile["name"] = user_name
            
            # Communication Style
            comm_style = st.selectbox(
                "Communication Style",
                ["gentle", "balanced", "direct"],
                index=["gentle", "balanced", "direct"].index(
                    st.session_state.user_profile["preferred_communication_style"]
                )
            )
            st.session_state.user_profile["preferred_communication_style"] = comm_style
            
            # Current Mood
            mood = st.select_slider(
                "How are you feeling today?",
                options=["very_low", "low", "neutral", "good", "very_good"],
                value=st.session_state.user_profile.get("emotional_state", "neutral")
            )
            st.session_state.user_profile["emotional_state"] = mood
            
            st.divider()
            
            # Context Information
            st.subheader("💭 Session Context")
            st.write(f"**Interactions:** {st.session_state.conversation_context['interaction_count']}")
            
            if st.session_state.conversation_context["topics_discussed"]:
                st.write("**Topics Discussed:**")
                for topic in st.session_state.conversation_context["topics_discussed"][-3:]:
                    st.write(f"• {topic}")
            
            # Clear conversation
            if st.button("🔄 New Conversation", type="secondary"):
                self.clear_conversation()
            
            # Export conversation
            if st.button("💾 Export Chat", type="secondary"):
                self.export_conversation()
    
    def render_main_chat(self):
        """Render the main chat interface"""
        # Title
        self.ui.render_title()
        
        # Display chat messages
        self.display_chat_history()
        
        # Chat input
        self.handle_user_input()
    
    def display_chat_history(self):
        """Display the chat history with enhanced formatting"""
        for message in st.session_state.messages[1:]:  # Skip system message
            if isinstance(message, HumanMessage):
                with st.chat_message("user", avatar="😊"):
                    st.markdown(message.content)
            elif isinstance(message, AIMessage):
                with st.chat_message("assistant", avatar="🌞"):
                    st.markdown(message.content)
    
    def handle_user_input(self):
        """Handle user input and generate responses"""
        user_input = st.chat_input("Tell me what's on your mind today! 💭")
        
        if user_input:
            # Update interaction count
            st.session_state.conversation_context["interaction_count"] += 1
            
            # Process user input through context engine
            processed_input = self.context_engine.process_user_input(
                user_input, 
                st.session_state.user_profile,
                st.session_state.conversation_context
            )
            
            # Display user message
            with st.chat_message("user", avatar="😊"):
                st.markdown(user_input)
            
            # Add to message history
            st.session_state.messages.append(HumanMessage(content=processed_input))
            
            # Generate and display AI response
            self.generate_ai_response()
    
    def generate_ai_response(self):
        """Generate AI response with context awareness"""
        try:
            with st.chat_message("assistant", avatar="🌞"):
                with st.spinner("Solara is thinking..."):
                    # Prepare context-aware messages
                    context_messages = self.context_engine.prepare_context_messages(
                        st.session_state.messages,
                        st.session_state.user_profile,
                        st.session_state.conversation_context
                    )
                    
                    # Generate response
                    response = self.llm.invoke(context_messages)
                    response_text = getattr(response, "content", str(response))
                    
                    # Post-process response
                    final_response = self.context_engine.post_process_response(
                        response_text,
                        st.session_state.user_profile,
                        st.session_state.conversation_context
                    )
                    
                    # Display response
                    st.markdown(final_response)
                    
                    # Add to message history
                    st.session_state.messages.append(AIMessage(content=final_response))
                    
                    # Update context
                    self.context_engine.update_conversation_context(
                        st.session_state.messages[-2].content,  # User message
                        final_response,  # AI response
                        st.session_state.conversation_context
                    )
                    
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            error_response = "I'm having trouble generating a response right now. Please try again in a moment. 🌙"
            st.error(error_response)
            st.session_state.messages.append(AIMessage(content=error_response))
    
    def clear_conversation(self):
        """Clear the conversation and reset context"""
        st.session_state.messages = []
        system_prompt = self.personality.get_enhanced_system_prompt()
        st.session_state.messages.append(SystemMessage(content=system_prompt))
        
        st.session_state.conversation_context = {
            "user_emotions": [],
            "topics_discussed": [],
            "session_start": datetime.now().isoformat(),
            "interaction_count": 0
        }
        st.rerun()
    
    def export_conversation(self):
        """Export conversation to text file"""
        try:
            conversation_text = self.context_engine.export_conversation(st.session_state.messages)
            st.download_button(
                label="Download Conversation",
                data=conversation_text,
                file_name=f"solara_conversation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain"
            )
        except Exception as e:
            logger.error(f"Error exporting conversation: {e}")
            st.error("Failed to export conversation")
    
    def run(self):
        """Main app runner"""
        if self.llm is None:
            st.error("Unable to start Solara. Please check your Ollama installation.")
            return
        
        # Render sidebar
        self.render_sidebar()
        
        # Render main chat interface
        self.render_main_chat()
        
        # Manage message history to prevent memory issues
        self.context_engine.manage_message_history(st.session_state.messages)

def main():
    """Main function to run the Solara app"""
    app = SolaraApp()
    app.run()

if __name__ == "__main__":
    main()