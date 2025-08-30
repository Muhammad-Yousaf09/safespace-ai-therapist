# SafeSpace 🧠 - Agentic AI Mental Therapist

A compassionate AI-powered mental health support system that provides empathetic therapeutic dialogue, emotional support, and crisis intervention through advanced agentic behavior and natural language processing.

## 🌟 Project Overview

SafeSpace is an innovative mental health support platform that leverages the power of AI agents to provide immediate, accessible, and empathetic mental health assistance. Built with responsible AI practices at its core, the system combines therapeutic expertise with cutting-edge technology to offer supportive conversations, evidence-based guidance, and emergency intervention capabilities.

### Key Features

- **🤖 Intelligent AI Therapist**: Powered by MedGemma medical language model with therapeutic personality
- **🚨 Crisis Detection & Response**: Automatic detection of suicidal ideation with emergency calling capabilities
- **📍 Local Resource Connection**: Find nearby licensed therapists and mental health professionals
- **💬 Empathetic Conversations**: Warm, supportive dialogue using evidence-based therapeutic techniques
- **🔒 Privacy-Focused**: Secure, confidential interactions with no data persistence
## 📂 Folder Structure

```
safespace-ai-therapist/
│── .venv/                 # Virtual environment  
│── __pycache__/           # Python cache files  
│── backend/               # Backend application logic  
│   │── __pycache__/  
│   │── ai_agent/          # AI agent implementation  
│   │── config/            # Configuration files (settings, API keys, etc.)  
│   │── main/              # Main backend entry point  
│   │── tools/             # Utility and helper functions  
│  
│── front_end/             # Frontend code (UI/Client)  
│── main.py                # Root entry point (launch script / app runner)  
│── pyproject.toml         # Project dependencies & metadata  
│── requirements.txt       # Python dependencies  
│── uv.lock                # Lock file for dependency management  
│── .python-version        # Python version info  
│── .gitignore             # Git ignore file  
│── README.md              # Project documentation  
```

---

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/ai-therapist.git
cd ai-therapist

## 🏗️ Architecture

The system follows a microservices architecture with three main components:

```
Frontend (Streamlit) → Backend (FastAPI) → AI Agent (LangGraph + Tools)
                                                ├── MedGemma Model
                                                ├── Emergency Calling (Twilio)
                                                └── Therapist Locator
```

## 🛠️ Technologies Used

- **Frontend**: Streamlit - Interactive web interface
- **Backend**: FastAPI - High-performance API framework
- **AI Framework**: LangChain/LangGraph - Agentic AI orchestration
- **Language Model**: OpenAI GPT-4 + MedGemma (Ollama)
- **Emergency Services**: Twilio API for crisis intervention
- **Python Libraries**: Pydantic, Requests, Uvicorn

## 📋 Prerequisites

- Python 3.8+
- OpenAI API Key
- Twilio Account (for emergency calling features)
- Ollama (for MedGemma model)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Muhammad-Yousaf09/safespace-ai-therapist.git
   cd safespace-ai-therapist
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Ollama and MedGemma model**
   ```bash
   # Install Ollama (visit ollama.ai for OS-specific instructions)
   ollama pull alibayram/medgemma:4b
   ```

4. **Configure environment**
   - Update `config.py` with your API keys:
     - `OPENAI_API_KEY`: Your OpenAI API key
     - `TWILIO_ACCOUNT_SID`: Your Twilio Account SID
     - `TWILIO_AUTH_TOKEN`: Your Twilio Auth Token
     - `TWILIO_FROM_NUMBER`: Your Twilio phone number
     - `EMERGENCY_CONTACT`: Emergency contact number

## 🎯 Usage

### Starting the Application

1. **Start the backend server**
   ```bash
   python main.py
   ```
   The API will be available at `http://127.0.0.1:8000`

2. **Launch the frontend**
   ```bash
   streamlit run front_end.py
   ```
   Access the web interface at `http://localhost:8501`

### Using SafeSpace

1. Open the web interface in your browser
2. Type your thoughts, concerns, or questions in the chat input
3. Receive empathetic, therapeutic responses from the AI
4. The system will automatically:
   - Provide supportive dialogue for general mental health concerns
   - Connect you with local therapists when requested
   - Initiate emergency calls if crisis indicators are detected

## 🤝 How It Works

### AI Agent Decision Making

The system uses an intelligent agent that chooses between three specialized tools:

1. **Mental Health Specialist Tool** (`ask_mental_health_specialist`)
   - Default response for emotional and psychological queries
   - Provides therapeutic guidance using MedGemma model
   - Maintains warm, empathetic conversation style

2. **Emergency Call Tool** (`emergency_call_tool`)
   - Automatically triggered for crisis situations
   - Detects suicidal ideation or self-harm intentions
   - Places immediate emergency calls via Twilio

3. **Therapist Locator Tool** (`find_nearby_therapists_by_location`)
   - Provides local mental health professional recommendations
   - Activated when users request professional help

### Therapeutic Approach

The AI therapist (Dr. Emily Hartman) is programmed with:
- **Emotional Attunement**: Recognizing and validating feelings
- **Gentle Normalization**: Reducing stigma around mental health
- **Practical Guidance**: Evidence-based coping strategies
- **Strengths-Based Support**: Highlighting user resilience

## ⚠️ Important Disclaimers

- **Not a Replacement for Professional Care**: SafeSpace is designed to complement, not replace, professional mental health services
- **Emergency Situations**: For immediate danger, please contact local emergency services (911, 988 Suicide & Crisis Lifeline)
- **Privacy**: Conversations are not stored, but emergency protocols may involve contacting designated emergency contacts
- **Scope Limitations**: The AI cannot provide official diagnoses or prescribe medications

## 🔧 Configuration

### Environment Variables

Create or modify `config.py` with the following required settings:

```python
TWILIO_ACCOUNT_SID = "your_twilio_sid"
TWILIO_AUTH_TOKEN = "your_twilio_token"
TWILIO_FROM_NUMBER = "your_twilio_number"
EMERGENCY_CONTACT = "emergency_contact_number"
OPENAI_API_KEY = "your_openai_api_key"
```

### Model Configuration

The system uses MedGemma with optimized parameters:
- Temperature: 0.7 (balanced creativity/accuracy)
- Top-p: 0.9 (diverse but relevant responses)
- Max tokens: 500 (comprehensive responses)

## 🧪 Testing

Test the different agent behaviors:

```python
# Test general mental health query
"I've been feeling anxious about my studies"

# Test therapist location request
"Can you help me find therapists near New York?"

# Test emergency detection (use with caution in development)
# System will detect crisis language and take appropriate action
```

## 🤝 Contributing

We welcome contributions that enhance the therapeutic capabilities and safety of SafeSpace:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/therapeutic-enhancement`)
3. Commit your changes (`git commit -am 'Add new coping strategy module'`)
4. Push to the branch (`git push origin feature/therapeutic-enhancement`)
5. Create a Pull Request

### Contribution Guidelines

- **Ethical AI**: Ensure all changes align with responsible AI practices
- **Clinical Accuracy**: Therapeutic content should be evidence-based
- **Safety First**: Prioritize user safety in all modifications
- **Privacy**: Maintain user confidentiality and data protection standards

## 📚 Research & References

This project is built on established therapeutic frameworks:
- Cognitive Behavioral Therapy (CBT) principles
- Dialectical Behavior Therapy (DBT) techniques
- Crisis intervention best practices
- Evidence-based mental health support methodologies

## 🔒 Privacy & Security

- **No Data Persistence**: Conversations are not stored or logged
- **Secure Communications**: All API calls use encrypted connections
- **Emergency Protocols**: Crisis detection follows established safety guidelines
- **Confidential**: User interactions remain private and anonymous

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Crisis Resources

If you or someone you know is in immediate danger:
- **US**: 988 Suicide & Crisis Lifeline
- **International**: Contact your local emergency services
- **Crisis Text Line**: Text HOME to 741741

## 👥 Contact & Support

- **Project Maintainer**: [Muhammad Yousaf]
- **Email**: [yousafzadran50@gmail.com]
- **Issues**: Please report bugs or feature requests via GitHub Issues
- **Security Concerns**: For security-related issues, please email privately

## 🙏 Acknowledgments

- **MedGemma Team**: For the specialized medical language model
- **Mental Health Professionals**: For guidance on therapeutic best practices
- **Open Source Community**: For the foundational tools and frameworks
- **Crisis Intervention Experts**: For safety protocol consultation

---

**Remember**: SafeSpace is designed to provide support and guidance, but professional mental health care remains essential for comprehensive treatment. Always prioritize your safety and well-being. 💙
