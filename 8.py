# Question: Find and list all severe JS errors

import asyncio
from pyppeteer import launch

async def get_js_errors(url):
    browser = await launch()
    page = await browser.newPage()

    # Collect JS errors
    errors = []
    page.on('pageerror', lambda err: errors.append(str(err)))

    await page.goto(url)
    await asyncio.sleep(3)  # wait for a bit to ensure JS execution

    await browser.close()
    return errors

url = input("Enter url: ") # e.g. https://mblessed.vercel.app
errors = asyncio.get_event_loop().run_until_complete(get_js_errors(url))
print("JS Errors:", errors)
