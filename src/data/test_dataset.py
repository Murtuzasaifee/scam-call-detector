test_calls = [
    {
        "type": "scam",
        "description": "Tech support scam",
        "sip_invite": """
INVITE sip:user@example.com SIP/2.0
Via: SIP/2.0/UDP spammer.scam.com;branch=z9hG4bK776asdhds
Max-Forwards: 70
To: User <sip:user@example.com>
From: "Tech Support" <sip:support@totallylegit.com>;tag=1928301774
Call-ID: a84b4c76e66710@spammer.scam.com
CSeq: 314159 INVITE
Contact: <sip:support@spammer.scam.com>
Content-Type: application/sdp
Content-Length: 142
        """,
        "transcription": """
Hello, this is Microsoft Tech Support. We've detected a virus on your computer. 
Your system is at risk. We need immediate access to your computer to remove the virus. 
Please provide us with your credit card information to validate your Windows license and proceed with the repair.
        """
    },
    {
        "type": "legitimate",
        "description": "Bank notification",
        "sip_invite": """
INVITE sip:customer@example.com SIP/2.0
Via: SIP/2.0/UDP bank.com;branch=z9hG4bK776asdhds
Max-Forwards: 70
To: Customer <sip:customer@example.com>
From: "Local Bank" <sip:notifications@bank.com>;tag=1928301774
Call-ID: a84b4c76e66710@bank.com
CSeq: 314159 INVITE
Contact: <sip:notifications@bank.com>
Content-Type: application/sdp
Content-Length: 142
        """,
        "transcription": """
Hello, this is an automated message from Local Bank. We are calling to inform you that your monthly statement is now available online. 
To view your statement, please log in to your online banking account. If you have any questions, please call our customer service number during business hours. 
Thank you for banking with Local Bank.
        """
    },
    {
        "type": "scam",
        "description": "IRS impersonation scam",
        "sip_invite": """
INVITE sip:victim@example.com SIP/2.0
Via: SIP/2.0/UDP scammer.fake-irs.com;branch=z9hG4bK776asdhds
Max-Forwards: 70
To: Victim <sip:victim@example.com>
From: "IRS Agent" <sip:agent@irs-totally-real.gov>;tag=1928301774
Call-ID: a84b4c76e66710@scammer.fake-irs.com
CSeq: 314159 INVITE
Contact: <sip:agent@scammer.fake-irs.com>
Content-Type: application/sdp
Content-Length: 142
        """,
        "transcription": """
This is Agent Johnson from the Internal Revenue Service. I'm calling about an urgent matter regarding your tax returns. 
There are serious allegations of tax evasion against you. If you don't resolve this immediately, we'll be forced to issue an arrest warrant. 
To avoid legal action, you must make a payment today using gift cards. Do not hang up or contact anyone else, or the police will be dispatched to your location.
        """
    },
    {
        "type": "legitimate",
        "description": "Doctor's appointment reminder",
        "sip_invite": """
INVITE sip:patient@example.com SIP/2.0
Via: SIP/2.0/UDP clinic.health.com;branch=z9hG4bK776asdhds
Max-Forwards: 70
To: Patient <sip:patient@example.com>
From: "City Health Clinic" <sip:reminders@clinic.health.com>;tag=1928301774
Call-ID: a84b4c76e66710@clinic.health.com
CSeq: 314159 INVITE
Contact: <sip:reminders@clinic.health.com>
Content-Type: application/sdp
Content-Length: 142
        """,
        "transcription": """
Hello, this is an automated reminder from City Health Clinic for John Doe. You have an appointment scheduled with Dr. Smith tomorrow at 2:00 PM. 
If you need to reschedule or have any questions, please call our office during business hours. 
Remember to bring your insurance card and any relevant medical records. Thank you for choosing City Health Clinic for your healthcare needs.
        """
    },
    {
        "type": "scam",
        "description": "Lottery scam",
        "sip_invite": """
INVITE sip:lucky-winner@example.com SIP/2.0
Via: SIP/2.0/UDP lotto-scam.com;branch=z9hG4bK776asdhds
Max-Forwards: 70
To: Lucky Winner <sip:lucky-winner@example.com>
From: "International Lottery" <sip:prize@big-win-lotto.com>;tag=1928301774
Call-ID: a84b4c76e66710@lotto-scam.com
CSeq: 314159 INVITE
Contact: <sip:prize@lotto-scam.com>
Content-Type: application/sdp
Content-Length: 142
        """,
        "transcription": """
Congratulations! You've won the International Mega Lottery! Your phone number was randomly selected as the grand prize winner of $5 million dollars. 
To claim your prize, we need you to wire a processing fee of $1000 to cover taxes and transfer costs. 
Once we receive the fee, we'll immediately transfer the full amount to your bank account. This is a limited time offer, so act now!
        """
    },
    {
        "type": "legitimate",
        "description": "Job interview invitation",
        "sip_invite": """
INVITE sip:applicant@example.com SIP/2.0
Via: SIP/2.0/UDP hr.company.com;branch=z9hG4bK776asdhds
Max-Forwards: 70
To: Job Applicant <sip:applicant@example.com>
From: "HR Department" <sip:hr@company.com>;tag=1928301774
Call-ID: a84b4c76e66710@hr.company.com
CSeq: 314159 INVITE
Contact: <sip:hr@company.com>
Content-Type: application/sdp
Content-Length: 142
        """,
        "transcription": """
Hello, this is Sarah from the HR department at TechCorp. I'm calling regarding your recent application for the Software Developer position. 
We were impressed with your resume and would like to invite you for an interview next week. 
Are you available on Tuesday at 10 AM for a video call? If that time doesn't work, please let me know and we can find an alternative. You can reach me at this number or via email at sarah@techcorp.com to confirm or reschedule.
        """
    }
]
