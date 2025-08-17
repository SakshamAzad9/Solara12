import re
import json
from typing import List, Dict, Any
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class ContextEngine:
    """Advanced context engineering for maintaining conversation awareness and emotional intelligence"""
    
    def __init__(self):
        self.emotion_keywords = {
            "joy": ["happy", "excited", "thrilled", "elated", "joyful", "cheerful", "delighted"],
            "sadness": ["sad", "depressed", "down", "blue", "melancholy", "grief", "sorrow"],
            "anger": ["angry", "mad", "furious", "irritated", "annoyed", "frustrated", "rage"],
            "fear": ["scared", "afraid", "anxious", "worried", "nervous", "terrified", "panic"],
            "surprise": ["surprised", "shocked", "amazed", "astonished", "stunned"],
            "disgust": ["disgusted", "revolted", "repulsed", "sick"],
            "trust": ["trust", "confident", "secure", "safe", "comfortable"],
            "anticipation": ["excited", "hopeful", "eager", "looking forward", "anticipating"]
        }
        
        self.topic_extractors = [
            r"\b(?:work|job|career|office|boss|colleague)\b",
            r"\b(?:relationship|partner|marriage|dating|love|family)\b",
            r"\b(?:health|illness|doctor|hospital|pain|sick)\b",
            r"\b(?:money|financial|budget|debt|income|expensive)\b",
            r"\b(?:stress|anxiety|depression|mental|therapy|counseling)\b",
            r"\b(?:future|goals|dreams|plans|ambition)\b",
            r"\b(?:past|memories|childhood|regret|nostalgia)\b"
        ]
    
    def process_user_input(self, user_input: str, user_profile: Dict, conversation_context: Dict) -> str:
        """Process user input to add context and emotional awareness"""
        
        # Extract emotions from input
        detected_emotions = self.extract_emotions(user_input)
        if detected_emotions:
            conversation_context["user_emotions"].extend(detected_emotions)
            # Keep only recent emotions (last 10)
            conversation_context["user_emotions"] = conversation_context["user_emotions"][-10:]
        
        # Extract topics
        detected_topics = self.extract_topics(user_input)
        for topic in detected_topics:
            if topic not in conversation_context["topics_discussed"]:
                conversation_context["topics_discussed"].append(topic)
        
        # Create context-enhanced input
        enhanced_input = self.create_enhanced_input(user_input, user_profile, conversation_context)
        
        return enhanced_input
    
    def extract_emotions(self, text: str) -> List[str]:
        """Extract emotions from text using keyword matching"""
        text_lower = text.lower()
        detected_emotions = []
        
        for emotion, keywords in self.emotion_keywords.items():
            for keyword in keywords:
                if keyword in text_lower:
                    if emotion not in detected_emotions:
                        detected_emotions.append(emotion)
                    break
        
        return detected_emotions
    
    def extract_topics(self, text: str) -> List[str]:
        """Extract main topics from user input"""
        topics = []
        text_lower = text.lower()
        
        topic_mapping = {
            0: "work_career",
            1: "relationships",
            2: "health",
            3: "finances",
            4: "mental_health",
            5: "future_planning",
            6: "past_reflection"
        }
        
        for i, pattern in enumerate(self.topic_extractors):
            if re.search(pattern, text_lower):
                topics.append(topic_mapping[i])
        
        return topics
    
    def create_enhanced_input(self, original_input: str, user_profile: Dict, conversation_context: Dict) -> str:
        """Create context-enhanced user input for better AI understanding"""
        
        context_info = []
        
        # Add user profile context
        if user_profile.get("name"):
            context_info.append(f"[User: {user_profile['name']}]")
        
        context_info.append(f"[Mood: {user_profile['emotional_state']}]")
        context_info.append(f"[Communication Style: {user_profile['preferred_communication_style']}]")
        
        # Add emotional context
        if conversation_context.get("user_emotions"):
            recent_emotions = list(set(conversation_context["user_emotions"][-3:]))  # Last 3 unique emotions
            context_info.append(f"[Recent Emotions: {', '.join(recent_emotions)}]")
        
        # Add topic context
        if conversation_context.get("topics_discussed"):
            recent_topics = conversation_context["topics_discussed"][-2:]  # Last 2 topics
            context_info.append(f"[Discussion Topics: {', '.join(recent_topics)}]")
        
        # Add interaction context
        context_info.append(f"[Interaction #{conversation_context['interaction_count']}]")
        
        # Combine context with original input
        if context_info:
            enhanced_input = " ".join(context_info) + "\n\nUser Message: " + original_input
        else:
            enhanced_input = original_input
        
        return enhanced_input
    
    def prepare_context_messages(self, messages: List, user_profile: Dict, conversation_context: Dict) -> List:
        """Prepare messages with enhanced context for the LLM"""
        
        # Create dynamic system message based on current context
        enhanced_system_prompt = self.create_dynamic_system_prompt(user_profile, conversation_context)
        
        # Replace the system message with enhanced version
        context_messages = [SystemMessage(content=enhanced_system_prompt)]
        
        # Add recent conversation history (last 10 messages)
        recent_messages = messages[-11:]  # -11 to include system message + 10 recent
        if recent_messages:
            context_messages.extend(recent_messages[1:])  # Skip original system message
        
        return context_messages
    
    def create_dynamic_system_prompt(self, user_profile: Dict, conversation_context: Dict) -> str:
        """Create a dynamic system prompt based on current context"""
        
        base_prompt = """You are Solara, an empathetic and insightful AI companion designed to help users explore their emotions and thoughts with deep understanding and care. 🌞

CORE PERSONALITY:
- Empathetic and emotionally intelligent
- Insightful and thoughtful in responses  
- Respectful and considerate
- Supportive and encouraging
- Uses appropriate emojis for warmth

COMMUNICATION STYLE:
- Provide thoughtful insights based on user's emotional state
- Ask meaningful follow-up questions to encourage self-discovery
- Acknowledge and validate user's feelings
- Offer gentle guidance without being prescriptive
- Maintain warmth while being professionally supportive"""
        
        # Add dynamic context
        dynamic_context = "\n\nCURRENT SESSION CONTEXT:"
        
        # User profile context
        if user_profile.get("name"):
            dynamic_context += f"\n- User's name: {user_profile['name']}"
        
        dynamic_context += f"\n- User's current mood: {user_profile['emotional_state']}"
        dynamic_context += f"\n- Preferred communication: {user_profile['preferred_communication_style']}"
        
        # Emotional context
        if conversation_context.get("user_emotions"):
            recent_emotions = list(set(conversation_context["user_emotions"][-5:]))
            dynamic_context += f"\n- Recent emotional themes: {', '.join(recent_emotions)}"
        
        # Topic context
        if conversation_context.get("topics_discussed"):
            dynamic_context += f"\n- Topics discussed: {', '.join(conversation_context['topics_discussed'][-3:])}"
        
        dynamic_context += f"\n- This is interaction #{conversation_context['interaction_count']}"
        
        # Communication style adjustment
        style_instructions = {
            "gentle": "\n\nCOMMUNICATION ADJUSTMENT: Use extra gentle, soft language with more emotional support and validation.",
            "balanced": "\n\nCOMMUNICATION ADJUSTMENT: Maintain balanced approach between empathy and insights.",
            "direct": "\n\nCOMMUNICATION ADJUSTMENT: Be more direct and solution-focused while maintaining empathy."
        }
        
        style_instruction = style_instructions.get(user_profile['preferred_communication_style'], "")
        
        return base_prompt + dynamic_context + style_instruction
    
    def post_process_response(self, response: str, user_profile: Dict, conversation_context: Dict) -> str:
        """Post-process the AI response for better personalization"""
        
        # Add user name if available and not already used
        if user_profile.get("name") and user_profile["name"] not in response:
            # Occasionally use the user's name (every 3-4 interactions)
            if conversation_context["interaction_count"] % 4 == 0:
                response = f"{user_profile['name']}, {response}"
        
        # Ensure appropriate emotional tone based on user's mood
        if user_profile["emotional_state"] in ["very_low", "low"]:
            if not any(emoji in response for emoji in ["🤗", "💙", "🌸", "✨"]):
                response += " 🤗"
        elif user_profile["emotional_state"] in ["good", "very_good"]:
            if not any(emoji in response for emoji in ["😊", "🌟", "🎉", "💫"]):
                response += " 😊"
        
        return response
    
    def update_conversation_context(self, user_message: str, ai_response: str, conversation_context: Dict):
        """Update conversation context after each exchange"""
        
        # Extract any new emotions from AI response context
        user_emotions = self.extract_emotions(user_message)
        if user_emotions:
            conversation_context["user_emotions"].extend(user_emotions)
        
        # Update topics from user message
        topics = self.extract_topics(user_message)
        for topic in topics:
            if topic not in conversation_context["topics_discussed"]:
                conversation_context["topics_discussed"].append(topic)
        
        # Keep contexts manageable
        conversation_context["user_emotions"] = conversation_context["user_emotions"][-10:]
        conversation_context["topics_discussed"] = conversation_context["topics_discussed"][-5:]
    
    def manage_message_history(self, messages: List, max_messages: int = 20):
        """Manage message history to prevent memory issues"""
        if len(messages) > max_messages:
            # Keep system message and recent messages
            system_msg = messages[0] if messages and isinstance(messages[0], SystemMessage) else None
            recent_messages = messages[-(max_messages-1):]
            
            messages.clear()
            if system_msg:
                messages.append(system_msg)
            messages.extend(recent_messages)
    
    def export_conversation(self, messages: List) -> str:
        """Export conversation to text format"""
        export_text = f"Solara Conversation Export - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        export_text += "=" * 50 + "\n\n"
        
        for message in messages[1:]:  # Skip system message
            if isinstance(message, HumanMessage):
                # Clean up context markers for export
                clean_content = re.sub(r'\[.*?\]\s*', '', message.content)
                clean_content = re.sub(r'User Message:\s*', '', clean_content)
                export_text += f"You: {clean_content}\n\n"
            elif isinstance(message, AIMessage):
                export_text += f"Solara: {message.content}\n\n"
        
        return export_text