from openai import OpenAI
import re
from datetime import datetime, timedelta
import yaml
import sys
import os


# Add the folder containing test_dataset.py to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Now you can import test_dataset
from data import test_dataset

class SpamCallDetector:
    def __init__(self):
        config_path = os.path.join(os.path.dirname(__file__), '../../configs/api_key.yaml')
        config = self.load_config(config_path)
        open_ai_key = config['openai']['api_key']
        print(open_ai_key)
        self.client = OpenAI(api_key=open_ai_key)
        self.call_history = {}

    def load_config(self, file_path):
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)
        return config

    def analyze_call(self, sip_message, transcription):
        # Extract relevant information from SIP message
        caller_id = self.extract_caller_id(sip_message)
        call_time = datetime.now()
        
        # Check call frequency
        frequency_info = self.check_call_frequency(caller_id, call_time)
        
        # Prepare the prompt for the LLM
        prompt = self.prepare_prompt(sip_message, frequency_info, transcription)
        
        # Get LLM's analysis
        analysis = self.get_llm_analysis(prompt)
        
        # Interpret LLM's response
        is_spam, reason = self.interpret_llm_response(analysis)
        
        return is_spam, reason

    def extract_caller_id(self, sip_message):
        match = re.search(r'From:\s*<sip:(.+?)@', sip_message)
        return match.group(1) if match else "Unknown"

    def check_call_frequency(self, caller_id, call_time):
        if caller_id not in self.call_history:
            self.call_history[caller_id] = []
        
        self.call_history[caller_id].append(call_time)
        
        # Remove calls older than 1 hour
        self.call_history[caller_id] = [t for t in self.call_history[caller_id] 
                                        if call_time - t <= timedelta(hours=1)]
        
        return f"Calls in the last hour: {len(self.call_history[caller_id])}"

    def prepare_prompt(self, sip_message, frequency_info, transcription):
        prompt = f"""
        Analyze the following information to determine if this call is likely to be spam or a scam:

        1. SIP Message:
        {sip_message}

        2. Call Frequency Information:
        {frequency_info}

        3. Call Transcription:
        {transcription}

        Consider the following in your analysis:
        - Any suspicious patterns in the SIP headers
        - Unusual call frequency
        - Content of the transcribed call, looking for:
          * Urgency or pressure tactics
          * Requests for personal information
          * Offers that seem too good to be true
          * Impersonation of authorities or well-known companies
          * Use of scripts or unnatural language patterns

        Provide a detailed analysis and conclude whether this is likely to be a spam or scam call. 
        If it is, explain why. If it's not, explain why it appears legitimate.
        """
        return prompt

    def get_llm_analysis(self, prompt):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert in analyzing calls for potential spam or scams. Provide a thorough analysis based on the given information."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content

    def interpret_llm_response(self, analysis):
        # This is a simple interpretation. You might want to make this more sophisticated.
        is_spam = "spam" in analysis.lower() or "scam" in analysis.lower()
        return is_spam, analysis

# Example usage
detector = SpamCallDetector()


# Using the test data from the previous example
for call in test_dataset.test_calls:
    print(f"Testing {call['type']} call: {call['description']}")
    
    is_spam, reason = detector.analyze_call(call['sip_invite'], call['transcription'])
    
    print(f"Detected as spam: {is_spam}")
    print(f"Analysis:\n{reason}")
    print("\n" + "="*50 + "\n")








