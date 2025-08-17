#!/usr/bin/env python3
"""
Solara Application Runner
Main entry point for the Solara conversational AI application
"""

import os
import sys
import logging
import argparse
from pathlib import Path

# Add the current directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

from config import get_config
import streamlit as st

def setup_logging(config):
    """Setup logging configuration"""
    logging.basicConfig(
        level=getattr(logging, config.LOG_LEVEL),
        format=config.LOG_FORMAT,
        handlers=[
            logging.FileHandler('solara.log'),
            logging.StreamHandler(sys.stdout)
        ]
    )

def check_requirements():
    """Check if all requirements are met"""
    try:
        import streamlit
        import langchain_ollama
        import langchain_core
        import plotly
        print("✅ All required packages are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing required package: {e}")
        print("Please install requirements: pip install -r requirements.txt")
        return False

def check_ollama():
    """Check if Ollama is running and has the required model"""
    try:
        from langchain_ollama import ChatOllama
        llm = ChatOllama(model="mistral")
        print("✅ Ollama is running and mistral model is available")
        return True
    except Exception as e:
        print(f"❌ Ollama check failed: {e}")
        print("Please ensure Ollama is running and mistral model is installed:")
        print("1. Install Ollama: https://ollama.ai")
        print("2. Run: ollama pull mistral")
        return False

def main():
    """Main application runner"""
    parser = argparse.ArgumentParser(description="Run Solara - Your Insightful Chat Companion")
    parser.add_argument(
        "--env", 
        choices=["development", "production", "testing"],
        default="development",
        help="Environment to run in (default: development)"
    )
    parser.add_argument(
        "--port", 
        type=int,
        default=8501,
        help="Port to run the application on (default: 8501)"
    )
    parser.add_argument(
        "--host",
        default="localhost",
        help="Host to run the application on (default: localhost)"
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Only check requirements and exit"
    )
    
    args = parser.parse_args()
    
    # Get configuration
    config = get_config(args.env)
    
    # Setup logging
    setup_logging(config)
    logger = logging.getLogger(__name__)
    
    logger.info(f"Starting Solara v{config.APP_VERSION} in {args.env} mode")
    
    # Create necessary directories
    config.create_directories()
    
    # Check requirements
    print("🔍 Checking system requirements...")
    if not check_requirements():
        sys.exit(1)
    
    if not check_ollama():
        sys.exit(1)
    
    if args.check_only:
        print("✅ All checks passed!")
        sys.exit(0)
    
    # Set environment variables for Streamlit
    os.environ['STREAMLIT_SERVER_PORT'] = str(args.port)
    os.environ['STREAMLIT_SERVER_ADDRESS'] = args.host
    os.environ['STREAMLIT_BROWSER_GATHER_USAGE_STATS'] = 'false'
    os.environ['STREAMLIT_SERVER_ENABLE_CORS'] = 'false'
    os.environ['STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION'] = 'false'
    
    # Application banner
    print("\n" + "="*60)
    print("🌞 SOLARA - Your Insightful Chat Companion")
    print(f"   Version: {config.APP_VERSION}")
    print(f"   Environment: {args.env}")
    print(f"   URL: http://{args.host}:{args.port}")
    print("="*60 + "\n")
    
    try:
        # Import and run the main app
        from app import main as run_app
        
        # Configure Streamlit to run our app
        if __name__ == "__main__":
            # Run via streamlit run command
            os.system(f"streamlit run app.py --server.port {args.port} --server.address {args.host}")
        else:
            # Run directly
            run_app()
            
    except KeyboardInterrupt:
        logger.info("Application stopped by user")
        print("\n👋 Thanks for using Solara! Take care!")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Application error: {e}")
        print(f"\n❌ Application error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()