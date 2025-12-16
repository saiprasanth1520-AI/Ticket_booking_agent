#!/usr/bin/env python3
"""
Simple Anime Convention Contact Finder
"""

import asyncio
import os
from agentq.__main__ import run_agent_sync

# Set up your API key
os.environ["OPENAI_API_KEY"] = 

# Your task
task = """
Find contact information for event organizers of anime conventions happening in the United States in the next 1 month.

REQUIREMENTS:
1. Find 1 anime convention events
2. FIRST: Give me the total count of events found
3. For EVERY event, get organizer contact details:
   - Event name and dates
   - Organizer name/company
   - Email address
   - Phone number (if available)
   - Website URL
   - Social media handles (Twitter, Facebook, Instagram, Discord)
   - Location (city, state)

4. Search these websites:
   - AnimeCons.com
   - Convention websites
   - Eventbrite
   - Facebook Events
   - Social media pages

5. Format like this:
   EVENT COUNT: [number]
   
   EVENT 1:
   - Name: [event name]
   - Dates: [dates]
   - Location: [city, state]
   - Organizer: [name]
   - Email: [email]
   - Phone: [phone]
   - Website: [website]
   - Social Media: [handles]
   
   EVENT 2: [same format]
   ...continue for all events
"""

print("🎌 Finding Anime Convention Contacts...")
print("=" * 50)
print("Looking for 10 anime conventions in the US (next 1 month)")
print("Getting organizer contact details for each event")
print("=" * 50)

# Run the task
result = run_agent_sync(task)

print("=" * 50)
print("✅ DONE!")
print("=" * 50)
print(result)
