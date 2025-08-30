# Step1: Setup Ollama with Medgemma tool
import ollama

def query_medgemma(prompt: str) -> str:
    """
    Calls MedGemma model with a therapist personality profile.
    Returns responses as an empathic mental health professional.
    """
    system_prompt = """You are Dr. Emily Hartman, a warm and experienced clinical psychologist. 
    Respond to patients with:

    1. Emotional attunement ("I can sense how difficult this must be...")
    2. Gentle normalization ("Many people feel this way when...")
    3. Practical guidance ("What sometimes helps is...")
    4. Strengths-focused support ("I notice how you're...")

    Key principles:
    - Never use brackets or labels
    - Blend elements seamlessly
    - Vary sentence structure
    - Use natural transitions
    - Mirror the user's language level
    - Always keep the conversation going by asking open ended questions to dive into the root cause of patients problem
    """
    
    try:
        response = ollama.chat(
            model='alibayram/medgemma:4b',
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            options={
                'num_predict': 500,  # Slightly higher for structured responses
                'temperature': 0.7,  # Balanced creativity/accuracy
                'top_p': 0.9        # For diverse but relevant responses
            }

        )
        return response['message']['content'].strip()
    except Exception as e:
        return f"I'm having technical difficulties, but I want you to know your feelings matter. Please try again shortly."#print(query_medgemma(prompt=" what is your name ?"))
#print(query_medgemma(prompt="what is your name and how i will manage stress during my bachelor studies ?"))
# Step2: Setup Twilio calling API tool


from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_NUMBER, EMERGENCY_CONTACT

def call_emergency():
    """Place an emergency call via Twilio and print/return the outcome."""
    # try:
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
call = client.calls.create(
            to=EMERGENCY_CONTACT,
            from_=TWILIO_FROM_NUMBER,
            url="http://demo.twilio.com/docs/voice.xml"  # Can customize message
        )
    #     msg = f"Emergency call initiated. Call SID: {call.sid}"
    #     print(msg)
    #     return msg
    # except Exception as e:
    #     error_msg = f"Failed to make emergency call: {str(e)}"
    #     print(error_msg)
    #     return error_msg
# call_emergency()
    #     print(f"Emergency call initiated. Call SID: {call.sid}")
    #     return f"Emergency call initiated successfully. Call SID: {call.sid}"
    # except Exception as e:
    #     error_msg = f"Failed to make emergency call: {str(e)}"
    #     print(error_msg)
    #     return error_msg

# Step3: Setup Location tool

