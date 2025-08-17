import os
from typing import Dict, Any

class Config:
    """Configuration settings for the Solara application"""
    
    # Application Settings
    APP_NAME = "Solara"
    APP_VERSION = "2.0.0"
    APP_DESCRIPTION = "Your Insightful Chat Companion"
    
    # LLM Settings
    DEFAULT_MODEL = "mistral"
    MODEL_TEMPERATURE = 0.7
    MODEL_TOP_P = 0.9
    MODEL_MAX_TOKENS = 2048
    
    # Context Management
    MAX_MESSAGE_HISTORY = 20
    MAX_EMOTIONS_TRACKED = 10
    MAX_TOPICS_TRACKED = 5
    CONTEXT_WINDOW_SIZE = 10
    
    # UI Settings
    PAGE_TITLE = f"{APP_NAME} - {APP_DESCRIPTION}"
    PAGE_ICON = "🌞"
    LAYOUT = "wide"
    SIDEBAR_STATE = "expanded"
    
    # Session Management
    SESSION_TIMEOUT_MINUTES = 60
    AUTO_SAVE_INTERVAL = 30  # seconds
    
    # Feature Flags
    ENABLE_EMOTION_TRACKING = True
    ENABLE_TOPIC_EXTRACTION = True
    ENABLE_CONVERSATION_EXPORT = True
    ENABLE_PERSONALITY_ADAPTATION = True
    ENABLE_ANALYTICS = True
    
    # Logging Settings
    LOG_LEVEL = "INFO"
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # Model Paths (for local models)
    MODELS_PATH = "./models/"
    
    # Data Storage
    CONVERSATIONS_PATH = "./data/conversations/"
    ANALYTICS_PATH = "./data/analytics/"
    USER_PROFILES_PATH = "./data/profiles/"
    
    @classmethod
    def get_model_config(cls) -> Dict[str, Any]:
        """Get model configuration"""
        return {
            "model": cls.DEFAULT_MODEL,
            "temperature": cls.MODEL_TEMPERATURE,
            "top_p": cls.MODEL_TOP_P,
            "max_tokens": cls.MODEL_MAX_TOKENS
        }
    
    @classmethod
    def get_ui_config(cls) -> Dict[str, Any]:
        """Get UI configuration"""
        return {
            "page_title": cls.PAGE_TITLE,
            "page_icon": cls.PAGE_ICON,
            "layout": cls.LAYOUT,
            "initial_sidebar_state": cls.SIDEBAR_STATE
        }
    
    @classmethod
    def get_context_config(cls) -> Dict[str, Any]:
        """Get context management configuration"""
        return {
            "max_message_history": cls.MAX_MESSAGE_HISTORY,
            "max_emotions_tracked": cls.MAX_EMOTIONS_TRACKED,
            "max_topics_tracked": cls.MAX_TOPICS_TRACKED,
            "context_window_size": cls.CONTEXT_WINDOW_SIZE
        }
    
    @classmethod
    def get_feature_flags(cls) -> Dict[str, bool]:
        """Get feature flags"""
        return {
            "emotion_tracking": cls.ENABLE_EMOTION_TRACKING,
            "topic_extraction": cls.ENABLE_TOPIC_EXTRACTION,
            "conversation_export": cls.ENABLE_CONVERSATION_EXPORT,
            "personality_adaptation": cls.ENABLE_PERSONALITY_ADAPTATION,
            "analytics": cls.ENABLE_ANALYTICS
        }
    
    @classmethod
    def create_directories(cls):
        """Create necessary directories if they don't exist"""
        directories = [
            cls.MODELS_PATH,
            cls.CONVERSATIONS_PATH,
            cls.ANALYTICS_PATH,
            cls.USER_PROFILES_PATH
        ]
        
        for directory in directories:
            os.makedirs(directory, exist_ok=True)

# Environment-specific configurations
class DevelopmentConfig(Config):
    """Development environment configuration"""
    LOG_LEVEL = "DEBUG"
    ENABLE_ANALYTICS = False

class ProductionConfig(Config):
    """Production environment configuration"""
    LOG_LEVEL = "WARNING"
    SESSION_TIMEOUT_MINUTES = 30
    AUTO_SAVE_INTERVAL = 60

class TestingConfig(Config):
    """Testing environment configuration"""
    LOG_LEVEL = "DEBUG"
    ENABLE_ANALYTICS = False
    MAX_MESSAGE_HISTORY = 5  # Smaller for testing

# Configuration factory
def get_config(env: str = "development") -> Config:
    """Get configuration based on environment"""
    configs = {
        "development": DevelopmentConfig,
        "production": ProductionConfig,
        "testing": TestingConfig
    }
    
    return configs.get(env.lower(), DevelopmentConfig)