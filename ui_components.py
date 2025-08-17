import streamlit as st
from typing import Dict, List, Any
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

class UIComponents:
    """Handles all UI components and styling for the Solara application"""
    
    def __init__(self):
        self.color_scheme = self._define_color_scheme()
        self.css_styles = self._define_css_styles()
    
    def _define_color_scheme(self) -> Dict[str, str]:
        """Define the application color scheme"""
        return {
            # Primary colors
            "primary_gold": "#f5d222",
            "primary_orange": "#ff8c00",
            "warm_yellow": "#ffd700",
            
            # Secondary colors  
            "soft_blue": "#87ceeb",
            "gentle_purple": "#dda0dd",
            "mint_green": "#98fb98",
            
            # Neutral colors
            "warm_white": "#fefefe",
            "light_gray": "#f5f5f5",
            "medium_gray": "#e0e0e0",
            "dark_gray": "#2f2f2f",
            
            # Background colors
            "chat_bg": "#1a1a1a",
            "user_msg_bg": "#2a2a2a",
            "assistant_msg_bg": "#1f1f1f",
            "sidebar_bg": "#0e1117",
            
            # Accent colors
            "success_green": "#90ee90",
            "warning_orange": "#ffa500",
            "error_red": "#ff6b6b",
            "info_blue": "#87ceeb"
        }
    
    def _define_css_styles(self) -> str:
        """Define custom CSS styles for the application"""
        colors = self.color_scheme
        
        return f"""
        <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@400;500;600&display=swap');
        
        /* Global Styles */
        .main {{
            background: linear-gradient(135deg, #0e1117 0%, #1a1a1a 100%);
            font-family: 'Inter', sans-serif;
        }}
        
        /* Custom Title Styling */
        .solara-title {{
            background: linear-gradient(45deg, {colors['primary_gold']}, {colors['primary_orange']}, {colors['warm_yellow']});
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-align: center;
            font-family: 'Playfair Display', serif;
            font-size: 2.5rem;
            font-weight: 600;
            margin-bottom: 1rem;
            text-shadow: 0 4px 8px rgba(245, 210, 34, 0.3);
        }}
        
        .solara-subtitle {{
            text-align: center;
            color: {colors['soft_blue']};
            font-size: 1.1rem;
            font-weight: 300;
            margin-bottom: 2rem;
            font-style: italic;
        }}
        
        /* Chat Message Styling */
        .stChatMessage {{
            border-radius: 15px;
            padding: 1rem;
            margin-bottom: 0.5rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            border: 1px solid rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
        }}
        
        .stChatMessage:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 16px rgba(0,0,0,0.2);
        }}
        
        /* User Message Styling */
        .stChatMessage[data-testid*="user"] {{
            background: linear-gradient(135deg, {colors['user_msg_bg']} 0%, #333 100%);
            border-left: 4px solid {colors['soft_blue']};
        }}
        
        /* Assistant Message Styling */
        .stChatMessage[data-testid*="assistant"] {{
            background: linear-gradient(135deg, {colors['assistant_msg_bg']} 0%, #2a2a2a 100%);
            border-left: 4px solid {colors['primary_gold']};
        }}
        
        /* Sidebar Styling */
        .css-1d391kg {{
            background: linear-gradient(180deg, {colors['sidebar_bg']} 0%, #1a1a1a 100%);
            border-right: 1px solid rgba(245, 210, 34, 0.2);
        }}
        
        /* Input Styling */
        .stTextInput input {{
            background: rgba(255,255,255,0.1) !important;
            border: 1px solid rgba(245, 210, 34, 0.3) !important;
            border-radius: 10px !important;
            color: white !important;
            font-size: 0.9rem !important;
            padding: 0.5rem !important;
        }}
        
        .stTextInput input:focus {{
            border-color: {colors['primary_gold']} !important;
            box-shadow: 0 0 10px rgba(245, 210, 34, 0.3) !important;
        }}
        
        /* Button Styling */
        .stButton button {{
            background: linear-gradient(45deg, {colors['primary_gold']}, {colors['primary_orange']});
            border: none;
            border-radius: 20px;
            color: black;
            font-weight: 500;
            padding: 0.5rem 1rem;
            transition: all 0.3s ease;
            box-shadow: 0 4px 8px rgba(245, 210, 34, 0.3);
        }}
        
        .stButton button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(245, 210, 34, 0.4);
            background: linear-gradient(45deg, {colors['warm_yellow']}, {colors['primary_gold']});
        }}
        
        /* Secondary Button Styling */
        .stButton button[kind="secondary"] {{
            background: transparent;
            border: 1px solid {colors['soft_blue']};
            color: {colors['soft_blue']};
        }}
        
        .stButton button[kind="secondary"]:hover {{
            background: {colors['soft_blue']};
            color: black;
        }}
        
        /* Select Box Styling */
        .stSelectbox div[data-baseweb="select"] {{
            background: rgba(255,255,255,0.1);
            border-radius: 10px;
            border: 1px solid rgba(245, 210, 34, 0.3);
        }}
        
        /* Slider Styling */
        .stSlider .css-1cpxqw2 {{
            background: linear-gradient(90deg, {colors['primary_gold']}, {colors['primary_orange']});
        }}
        
        /* Metrics and Stats */
        .metric-card {{
            background: rgba(255,255,255,0.05);
            border-radius: 15px;
            padding: 1rem;
            border: 1px solid rgba(245, 210, 34, 0.2);
            text-align: center;
            backdrop-filter: blur(10px);
        }}
        
        .metric-value {{
            font-size: 1.5rem;
            font-weight: 600;
            color: {colors['primary_gold']};
        }}
        
        .metric-label {{
            font-size: 0.9rem;
            color: {colors['soft_blue']};
            margin-top: 0.5rem;
        }}
        
        /* Emotion Indicators */
        .emotion-tag {{
            display: inline-block;
            background: rgba(245, 210, 34, 0.2);
            color: {colors['primary_gold']};
            padding: 0.25rem 0.5rem;
            border-radius: 20px;
            font-size: 0.8rem;
            margin: 0.25rem;
            border: 1px solid rgba(245, 210, 34, 0.3);
        }}
        
        /* Loading Animation */
        .solara-loading {{
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 2rem;
        }}
        
        .solara-spinner {{
            border: 3px solid rgba(245, 210, 34, 0.3);
            border-top: 3px solid {colors['primary_gold']};
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
        }}
        
        @keyframes spin {{
            0% {{ transform: rotate(0deg); }}
            100% {{ transform: rotate(360deg); }}
        }}
        
        /* Custom Scrollbar */
        .stChatFloatingInputContainer {{
            background: rgba(0,0,0,0.8);
            backdrop-filter: blur(10px);
            border-top: 1px solid rgba(245, 210, 34, 0.2);
        }}
        
        /* Toast Notifications */
        .stToast {{
            background: rgba(245, 210, 34, 0.1);
            border: 1px solid {colors['primary_gold']};
            color: white;
        }}
        
        /* Hide Streamlit Elements */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header {{visibility: hidden;}}
        
        /* Responsive Design */
        @media (max-width: 768px) {{
            .solara-title {{
                font-size: 2rem;
            }}
            .stChatMessage {{
                padding: 0.75rem;
            }}
        }}
        </style>
        """
    
    def apply_custom_styling(self):
        """Apply custom CSS styling to the Streamlit app"""
        st.markdown(self.css_styles, unsafe_allow_html=True)
    
    def render_title(self):
        """Render the main title with custom styling"""
        st.markdown("""
        <div class="solara-title">
            🌞 Solara - Your Insightful Companion
        </div>
        <div class="solara-subtitle">
            Where empathy meets understanding, and every conversation lights the way to self-discovery ✨
        </div>
        """, unsafe_allow_html=True)
    
    def render_metric_card(self, title: str, value: str, icon: str = "📊"):
        """Render a metric card with custom styling"""
        return f"""
        <div class="metric-card">
            <div style="font-size: 1.2rem; margin-bottom: 0.5rem;">{icon}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-label">{title}</div>
        </div>
        """
    
    def render_emotion_tags(self, emotions: List[str]) -> str:
        """Render emotion tags with custom styling"""
        if not emotions:
            return ""
        
        emotion_icons = {
            "joy": "😊", "happiness": "😊", "excited": "🤩",
            "sadness": "😢", "sad": "😢", "grief": "💙",
            "anger": "😠", "frustrated": "😤", "annoyed": "😑",
            "fear": "😰", "anxiety": "😟", "worried": "😟",
            "surprise": "😮", "amazed": "🤩", "shocked": "😲",
            "trust": "🤗", "confident": "💪", "secure": "🛡️",
            "anticipation": "🎯", "hopeful": "🌟", "eager": "✨"
        }
        
        tags_html = ""
        for emotion in emotions[-5:]:  # Show last 5 emotions
            icon = emotion_icons.get(emotion.lower(), "💭")
            tags_html += f'<span class="emotion-tag">{icon} {emotion.title()}</span>'
        
        return f'<div style="margin: 0.5rem 0;">{tags_html}</div>'
    
    def render_conversation_stats(self, conversation_context: Dict):
        """Render conversation statistics"""
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(
                self.render_metric_card(
                    "Interactions", 
                    str(conversation_context.get("interaction_count", 0)),
                    "💬"
                ), 
                unsafe_allow_html=True
            )
        
        with col2:
            topics_count = len(conversation_context.get("topics_discussed", []))
            st.markdown(
                self.render_metric_card(
                    "Topics Explored", 
                    str(topics_count),
                    "🧭"
                ), 
                unsafe_allow_html=True
            )
        
        with col3:
            emotions_count = len(set(conversation_context.get("user_emotions", [])))
            st.markdown(
                self.render_metric_card(
                    "Emotions Recognized", 
                    str(emotions_count),
                    "💝"
                ), 
                unsafe_allow_html=True
            )
    
    def render_emotion_timeline(self, conversation_context: Dict):
        """Render an emotion timeline visualization"""
        emotions = conversation_context.get("user_emotions", [])
        if not emotions:
            st.info("No emotions tracked yet. Start chatting to see your emotional journey! 💫")
            return
        
        # Create emotion timeline data
        emotion_counts = {}
        for emotion in emotions:
            emotion_counts[emotion] = emotion_counts.get(emotion, 0) + 1
        
        # Create pie chart for emotion distribution
        if emotion_counts:
            fig = px.pie(
                values=list(emotion_counts.values()),
                names=list(emotion_counts.keys()),
                title="Your Emotional Landscape 🎨",
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='white',
                title_font_size=16,
                showlegend=True
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    def render_loading_spinner(self, message: str = "Solara is thinking..."):
        """Render a custom loading spinner"""
        return f"""
        <div class="solara-loading">
            <div class="solara-spinner"></div>
            <div style="margin-left: 1rem; color: #87ceeb;">{message}</div>
        </div>
        """
    
    def render_welcome_message(self, user_name: str = "") -> str:
        """Render a personalized welcome message"""
        name_part = f" {user_name}" if user_name else ""
        
        return f"""
        <div style="text-align: center; padding: 2rem; background: rgba(245, 210, 34, 0.1); 
                    border-radius: 20px; margin: 1rem 0; border: 1px solid rgba(245, 210, 34, 0.3);">
            <h2 style="color: #f5d222; margin-bottom: 1rem;">Welcome{name_part}! 🌞</h2>
            <p style="color: #87ceeb; font-size: 1.1rem; line-height: 1.6;">
                I'm Solara, your empathetic AI companion. I'm here to listen deeply, understand genuinely, 
                and help you explore the landscape of your inner world. Whether you're celebrating joys, 
                working through challenges, or simply want to reflect on life, I'm here with you every step of the way. ✨
            </p>
            <p style="color: #dda0dd; font-style: italic; margin-top: 1rem;">
                What's on your heart today? 💝
            </p>
        </div>
        """
    
    def render_topic_cloud(self, topics: List[str]):
        """Render a visual topic cloud"""
        if not topics:
            return
        
        topic_display_names = {
            "work_career": "💼 Career",
            "relationships": "💕 Relationships", 
            "health": "🏥 Health",
            "finances": "💰 Finances",
            "mental_health": "🧠 Mental Health",
            "future_planning": "🎯 Future Plans",
            "past_reflection": "📚 Past Reflection"
        }
        
        st.subheader("🏷️ Topics We've Explored")
        
        topic_html = '<div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1rem 0;">'
        for topic in topics:
            display_name = topic_display_names.get(topic, f"💭 {topic.replace('_', ' ').title()}")
            topic_html += f'''
            <span style="
                background: rgba(245, 210, 34, 0.2);
                color: #f5d222;
                padding: 0.5rem 1rem;
                border-radius: 25px;
                font-size: 0.9rem;
                border: 1px solid rgba(245, 210, 34, 0.3);
                display: inline-block;
            ">{display_name}</span>
            '''
        topic_html += '</div>'
        
        st.markdown(topic_html, unsafe_allow_html=True)