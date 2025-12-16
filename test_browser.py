#!/usr/bin/env python3
"""
Test browser connectivity and navigation
"""

import asyncio
import os
from playwright.async_api import async_playwright

async def test_browser():
    """Test if browser can load websites"""
    print("🔍 Testing browser connectivity...")
    
    try:
        async with async_playwright() as p:
            # Try to launch browser
            print("📱 Launching browser...")
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()
            
            # Test 1: Try Google
            print("🌐 Testing Google...")
            try:
                await page.goto("https://www.google.com", timeout=10000)
                print("✅ Google loaded successfully")
            except Exception as e:
                print(f"❌ Google failed: {e}")
            
            # Test 2: Try Eventbrite
            print("🎫 Testing Eventbrite...")
            try:
                await page.goto("https://www.eventbrite.com", timeout=10000)
                print("✅ Eventbrite loaded successfully")
            except Exception as e:
                print(f"❌ Eventbrite failed: {e}")
            
            # Test 3: Try a simple site
            print("🔗 Testing simple site...")
            try:
                await page.goto("https://httpbin.org/get", timeout=10000)
                print("✅ Simple site loaded successfully")
            except Exception as e:
                print(f"❌ Simple site failed: {e}")
            
            await browser.close()
            print("🏁 Browser test completed")
            
    except Exception as e:
        print(f"💥 Browser launch failed: {e}")

if __name__ == "__main__":
    asyncio.run(test_browser())