# 🌞 Solara - AI Conversational Companion

<div align="center">
  <img src="sol.png" alt="Solara Logo" width="600" height="600" style="background: transparent;"/>
  
  **Your Private, On-Device Emotional Intelligence Companion**
  
  *Think of Solara as a private, on-device emotional intelligence companion that helps you explore your inner world through meaningful conversations.*
  
  [![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
  [![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
  [![LangChain](https://img.shields.io/badge/LangChain-Latest-green.svg)](https://langchain.com)
  [![Ollama](https://img.shields.io/badge/Ollama-Private_AI-orange.svg)](https://ollama.ai)
  [![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
  [![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](CONTRIBUTING.md)
</div>

---

## 🎯 Overview

Solara is an advanced conversational AI application that combines emotional intelligence with sophisticated context engineering. Built for meaningful conversations, self-discovery, and emotional support with complete privacy through local AI processing.

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Frontend** | 🖥️ Streamlit | Interactive web interface with custom styling |
| **AI Model** | 🧠 Mistral 7B | Core conversational intelligence |
| **Integration** | 🔗 LangChain + Ollama | Local model orchestration and management |
| **Visualization** | 📊 Plotly | Interactive charts for emotion tracking |
| **Data Processing** | 🐼 Pandas, NumPy | Context analysis and pattern recognition |
| **Styling** | 🎨 Custom CSS | Modern UI with gradients and animations |

## ✨ Core Features

### 🧠 **Advanced Context Engineering**
- **Dynamic Memory Management**: Maintains conversation context across sessions
- **Emotion Recognition**: Automatically detects and tracks 8+ emotion categories
- **Topic Extraction**: Identifies discussion themes (work, relationships, health, etc.)
- **Contextual Prompting**: Enhances AI responses with conversation history

### 💝 **Empathetic AI Personality**
- **Adaptive Communication**: 3 communication styles (Gentle/Balanced/Direct)
- **Emotional Intelligence**: Responds appropriately to user's emotional state
- **Thoughtful Insights**: Provides meaningful perspectives for self-discovery
- **Validation & Support**: Acknowledges feelings with genuine empathy

### 🎨 **Modern User Interface**
- **Beautiful Design**: Gradient backgrounds, smooth animations, custom components
- **Responsive Layout**: Optimized for desktop and mobile devices
- **Interactive Sidebar**: User profile, mood tracking, session controls
- **Visual Analytics**: Emotion timelines, topic clouds, conversation metrics

### 📊 **Smart Analytics**
- **Emotion Tracking**: Visual representation of emotional journey
- **Conversation Insights**: Topic distribution and interaction statistics  
- **Export Functionality**: Download chat history for reflection
- **Progress Visualization**: Charts showing emotional patterns over time

## 🚀 Installation Guide

### Step 1: System Requirements
```bash
# Required software
✅ Python 3.8 or higher
✅ Git (for cloning)
✅ 4GB+ RAM recommended
✅ Internet connection (for initial setup)
```

### Step 2: Install Ollama
<details>
<summary>📥 Ollama Installation Instructions</summary>

**Windows:**
```bash
# Download and run installer from https://ollama.ai
# Or use winget
winget install Ollama.Ollama
```

**macOS:**
```bash
# Download from https://ollama.ai
# Or use Homebrew
brew install ollama
```

**Linux:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

**Verify Installation:**
```bash
ollama --version
```
</details>

### Step 3: Setup Mistral Model
```bash
# Start Ollama service
ollama serve

# In a new terminal, pull the Mistral model
ollama pull mistral

# Verify model installation
ollama list
```

### Step 4: Install Solara
<details>
<summary>📦 Project Setup</summary>

```bash
# Method 1: Clone repository (if available)
git clone <repository-url>
cd solara-ai

# Method 2: Manual setup
mkdir solara-ai
cd solara-ai
# Copy all provided files to this directory
```
</details>

### Step 5: Install Python Dependencies
```bash
# Create virtual environment (recommended)
python -m venv solara-env

# Activate virtual environment
# Windows:
solara-env\Scripts\activate
# macOS/Linux:
source solara-env/bin/activate

# Install requirements
pip install -r requirements.txt
```

### Step 6: Launch Application
```bash
# Method 1: Using run script (recommended)
python run.py

# Method 2: Direct Streamlit
streamlit run app.py

# Method 3: Custom configuration
python run.py --port 8080 --host 0.0.0.0
```

### Step 7: Access Solara
```bash
🌐 Open your browser and navigate to:
http://localhost:8501

🎉 Welcome to Solara!
```

## 📁 Project Structure

```
solara-ai/
├── 📱 app.py              # Main Streamlit application
├── 🧠 context_engine.py   # Context management & emotion tracking
├── 💝 personality.py      # AI personality & response patterns
├── 🎨 ui_components.py    # Custom UI components & styling
├── ⚙️ config.py           # Configuration management
├── 🚀 run.py              # Application runner
├── 📦 requirements.txt    # Dependencies
├── 📖 README.md           # This documentation
├── 🖼️ sol.png            # Application logo
└── 📄 CONTRIBUTING.md     # Contribution guidelines
```

## 🎯 Key Features Deep Dive

<details>
<summary>🧠 Context Engineering System</summary>

```python
# Automatic emotion detection from 8 categories
emotions = ["joy", "sadness", "anger", "fear", "surprise", "trust", "anticipation", "disgust"]

# Topic extraction patterns
topics = ["work_career", "relationships", "health", "finances", "mental_health", "future_planning"]

# Dynamic context building
enhanced_prompt = f"[User: {name}] [Mood: {mood}] [Recent Emotions: {emotions}] {user_input}"
```
</details>

<details>
<summary>💝 Personality Adaptation System</summary>

```python
# Personality traits (1-10 scale)
traits = {
    "empathy": 9,      # High emotional understanding
    "insight": 8,      # Thoughtful perspectives  
    "warmth": 9,       # Caring communication
    "patience": 10,    # Never rushed responses
    "authenticity": 8  # Genuine interactions
}
```
</details>

<details>
<summary>🎨 UI Components</summary>

- **Metric Cards**: Show conversation statistics
- **Emotion Tags**: Visual emotion indicators
- **Topic Clouds**: Interactive discussion themes
- **Custom Chat Bubbles**: Styled message containers
- **Analytics Charts**: Plotly-powered visualizations
</details>

## 🔧 Configuration

### Communication Styles
- **Gentle**: Extra soft language, maximum emotional support
- **Balanced**: Mix of empathy and practical insights  
- **Direct**: Solution-focused while maintaining warmth

<details>
<summary>⚙️ Advanced Settings</summary>

```python
# Model Configuration
DEFAULT_MODEL = "mistral"
TEMPERATURE = 0.7
MAX_TOKENS = 2048
CONTEXT_WINDOW = 20

# Feature Toggles
ENABLE_EMOTION_TRACKING = True
ENABLE_TOPIC_EXTRACTION = True  
ENABLE_ANALYTICS = True
ENABLE_EXPORT = True
```
</details>

## 💡 Usage Examples

### Starting Conversations

**User**: I've been feeling overwhelmed with work lately...  
**Solara**: I can sense the weight you're carrying with work right now 💙 That feeling of being overwhelmed often comes when we have more on our plate than feels manageable. What aspect of work is feeling most heavy today?

**User**: I'm excited about a new opportunity but also scared...  
**Solara**: What beautiful awareness you have! ✨ It's so human to feel both excitement and fear when something meaningful is on the horizon. These mixed feelings often show up when something really matters to us. What part of this opportunity feels most exciting to you?

### Analytics Features
- 📈 View emotional journey over time
- 🏷️ Track discussion topics
- 💾 Export conversations for reflection
- 📊 Monitor interaction patterns

## 🛠️ Development

### Running Different Modes
```bash
# Development mode (debug logging)
python run.py --env development

# Production mode (optimized)
python run.py --env production

# Custom port/host
python run.py --port 8080 --host 0.0.0.0

# System check only
python run.py --check-only
```

### Extending Features
- **New Emotions**: Add to `emotion_keywords` in `context_engine.py`
- **Custom UI**: Modify components in `ui_components.py`
- **Personality Traits**: Extend traits in `personality.py`
- **Analytics**: Add charts in UI components

## 🔍 Troubleshooting

| Issue | Solution | Additional Help |
|-------|----------|----------------|
| LLM initialization fails | Verify Ollama is running: `ollama serve` | [Ollama Docs](https://ollama.ai/docs) |
| Missing dependencies | Run: `pip install -r requirements.txt` | [Python Package Issues](https://github.com/solara-ai/issues) |
| UI styling broken | Clear browser cache or try incognito mode | [UI Issues](https://github.com/solara-ai/issues) |
| Memory issues | Reduce `MAX_MESSAGE_HISTORY` in config | [Performance Guide](https://github.com/solara-ai/wiki) |
| Port conflicts | Use: `python run.py --port 8080` | [Configuration Help](https://github.com/solara-ai/discussions) |

## 🌟 What Makes Solara Special

1. **🔒 Complete Privacy**: Local AI processing, no data leaves your device
2. **🧠 Emotional Intelligence**: Advanced emotion recognition and appropriate responses
3. **💭 Context Awareness**: Maintains meaningful conversation flow across sessions
4. **🎨 Beautiful Interface**: Professional design with smooth animations
5. **🎯 Personality Adaptation**: Adjusts to user preferences and emotional state
6. **📊 Insightful Analytics**: Deep insights into emotional patterns and themes
7. **💾 Export Features**: Save conversations for personal reflection and growth

## 📊 Performance Metrics

- **⚡ Response Time**: < 2 seconds (local processing)
- **🧠 Context Window**: 20 messages with intelligent pruning
- **💝 Emotion Categories**: 8 primary emotions automatically tracked
- **🏷️ Topic Categories**: 7 life areas automatically identified
- **⚡ Memory Efficiency**: Dynamic context management prevents memory bloat
- **🔒 Privacy**: 100% local processing, zero external API calls

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Ways to contribute:**
- 🧠 Add new emotion recognition patterns
- 🎨 Create custom UI themes
- 💝 Implement additional personality traits
- 📊 Build new analytics features
- 🏷️ Expand topic extraction capabilities

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

> 🌞 **Solara** — Every conversation lights the way to self-discovery ✨  
> Built with ❤️ using Streamlit, LangChain & Ollama
