#!/usr/bin/env python3
"""
Projectz AI signup, walkthrough, and product review.

Steps the agent will perform:
- Sign up on https://projectzai.com/ with the provided credentials.
- Explore design flows, project organization tools, and contractor features.
- Produce insights, propose the first ML feature, suggest AI UX improvements,
  and outline a 30-day impact plan.
"""

import asyncio
from agentq.__main__ import run_agent_sync

# Task prompt for the AgentQ runner.
task = """
You are a product analyst. Complete these steps in the browser and then report findings:

1) Sign up on https://projectzai.com/
   - First name: sai
   - Last name: p
   - Email: saiprasanthpaladugula531@gmail.com
   - Password: Prasanth@2000
   - If the account already exists, try to sign in with the same credentials; if login fails, report what you saw.

2) After signing up (or logging in), explore and review:
   - Design flows
   - Project organization tools
   - Contractor features (e.g., collaboration, task assignment, tracking)

3) Final output: provide a concise written summary with these sections:
   - Insights: key observations about design flows, project org tools, contractor features.
   - First ML feature to build: one high-impact ML capability tailored to the platform.
   - AI UX improvements: short analysis of how AI can improve Projectz AI user experience.
   - 30-day plan: a lightweight plan for impact (week-by-week bullets).

General rules:
- Navigate carefully; if blocked or forms fail, describe what happened.
- Keep the final response concise and structured.
"""


def main():
    print("🚀 Projectz AI signup and review starting...")
    result = run_agent_sync(task)
    print("✅ Task completed. Summary:")
    print(result)


if __name__ == "__main__":
    if asyncio.get_event_loop().is_closed():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    main()

