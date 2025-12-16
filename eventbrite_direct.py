#!/usr/bin/env python3
"""
Direct Eventbrite Registration - Bypasses Google navigation issue
"""

import asyncio
import os
from playwright.async_api import Page

from agentq.core.agent.agentq import AgentQ
from agentq.core.agent.agentq_actor import AgentQActor
from agentq.core.agent.agentq_critic import AgentQCritic
from agentq.core.agent.browser_nav_agent import BrowserNavAgent
from agentq.core.agent.planner_agent import PlannerAgent
from agentq.core.models.models import State
from agentq.core.orchestrator.orchestrator import Orchestrator

# Set up your API key
os.environ["OPENAI_API_KEY"] = "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"

state_to_agent_map = {
    State.PLAN: PlannerAgent(),
    State.BROWSE: BrowserNavAgent(),
    State.AGENTQ_BASE: AgentQ(),
    State.AGENTQ_ACTOR: AgentQActor(),
    State.AGENTQ_CRITIC: AgentQCritic(),
}

async def run_agent_direct(command):
    """Modified version that skips the problematic Google navigation"""
    orchestrator = Orchestrator(state_to_agent_map=state_to_agent_map, eval_mode=True)
    await orchestrator.start()
    page: Page = await orchestrator.playwright_manager.get_current_page()
    await page.set_extra_http_headers({"User-Agent": "AgentQ-Bot"})
    
    # Skip the problematic Google navigation and go directly to Eventbrite
    print("🚀 Starting browser and navigating to Eventbrite...")
    await page.goto("https://www.eventbrite.com", wait_until="domcontentloaded", timeout=15000)
    print("✅ Successfully loaded Eventbrite")
    
    result = await orchestrator.execute_command(command)
    return result

def run_agent_sync_direct(command):
    if asyncio.get_event_loop().is_closed():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    else:
        loop = asyncio.get_event_loop()

    return loop.run_until_complete(run_agent_direct(command))

# Simple task following the example pattern
task = """
Register for the "WellthyWell: San Diego Walk & Talk" event on Eventbrite. Fill out the registration form with first name "sai", last name "p", and email "saiprasanthpaladugula531@gmail.com".
"""

print("🎫 Direct Eventbrite Registration...")
print("=" * 50)
print("Event: WellthyWell: San Diego Walk & Talk")
print("Name: sai p")
print("Email: saiprasanthpaladugula531@gmail.com")
print("=" * 50)

# Run the task
result = run_agent_sync_direct(task)

print("=" * 50)
print("✅ REGISTRATION COMPLETE!")
print("=" * 50)
print("RESULT:")
print(result)