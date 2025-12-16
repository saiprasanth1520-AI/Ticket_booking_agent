#!/usr/bin/env python3
"""
Simple Eventbrite Registration Task
Based on example task patterns from the codebase
"""

import asyncio
import os
from agentq.__main__ import run_agent_sync

# Set up your API key
os.environ["OPENAI_API_KEY"] = 

# Simple task following the example pattern
task = """
Go to the website dosd.com. Search for the event titled: "Tributo a Luis Miguel / Alejandro Sanz". Find the event scheduled for September 17.
Open the event page and proceed to registration or ticket selection.In the ticket dropdown, select 1 ticket. Click on Checkout or Register to proceed.
Fill in the contact details on the form: First Name: sai, Last Name: sai, Email: saiprasanthpaladugula531@gmail.com, Phone: 9999999999
Check any required checkboxes (e.g., terms, newsletter, etc.)
Click on “Place Order” or the equivalent button to complete registration.
"""

print("🎫 Simple Registration for Tributo a Luis Miguel / Alejandro Sanz...")
print("=" * 50)
print("Event: Tributo a Luis Miguel / Alejandro Sanz")
print("Name: sai p")
print("Email: saiprasanthpaladugula531@gmail.com")
print("=" * 50)

# Run the task
result = run_agent_sync(task)

print("=" * 50)
print("✅ REGISTRATION COMPLETE!")
print("=" * 50)
print("RESULT:")
print(result)
