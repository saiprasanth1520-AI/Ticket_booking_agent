#!/usr/bin/env python3
"""
Detailed Eventbrite Registration Task
Step-by-step registration for WellthyWell: San Diego Walk & Talk
"""

import asyncio
import os
from agentq.__main__ import run_agent_sync

# Set up your API key
os.environ["OPENAI_API_KEY"] = "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"

# Enhanced task with specific SVG targeting
task = """
Register for the "WellthyWell: San Diego Walk & Talk" event on Eventbrite.

STEP-BY-STEP INSTRUCTIONS:

1. Go to www.eventbrite.com
2. Search for "WellthyWell: San Diego Walk & Talk"
3. Click on the event that shows "San Diego" and "Saturday" or "Sunday"
4. On the event page, find the ticket section with "General Admission" tickets
5. Look for "Register" button (not "Get tickets") and click it
6. After clicking "Register", wait for the page (wait up to 30 seconds) to load and look for:
   - A registration/checkout form with input fields for contact information can be found in the form
7. fill the fields in that with:
   - First name: sai
   - Last name: p
   - Email: saiprasanthpaladugula531@gmail.com
8. Check boxes for: Keep me updated on more events and news from this event organizer, and Send me emails about the best events happening nearby or online.
9. click on register button to complete the registration

CRITICAL RULES:
- Look for "Register" button (not "Get tickets") and click it
- Click "Register" button to proceed to registration form
- After clicking "Register", look for a form or checkout page
- If no form appears after clicking "Register", report what you see
- Do NOT keep clicking buttons repeatedly
- If you see a form, proceed with filling it out
"""

print("🎫 Detailed Eventbrite Registration...")
print("=" * 60)
print("Event: WellthyWell: San Diego Walk & Talk")
print("Location: San Diego")
print("Date: This weekend (Saturday or Sunday)")
print("Tickets: 1 free ticket")
print("Name: sai p")
print("Email: saiprasanthpaladugula531@gmail.com")
print("=" * 60)

# Run the task
result = run_agent_sync(task)

print("=" * 60)
print("✅ REGISTRATION COMPLETE!")
print("=" * 60)
print("RESULT:")
print(result)