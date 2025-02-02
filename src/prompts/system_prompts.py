def prepare_prompt(sip_message, frequency_info, transcription):
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