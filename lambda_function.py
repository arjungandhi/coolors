import asyncio
from pyppeteer import launch
import json

def lambda_handler(event, context):
    loop = asyncio.get_event_loop()
    r = loop.run_until_complete(main())
    result = r.split('/')[-1]
    result = result.split('-')

    print(result)

    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }

async def main():
    browser = await launch(headless=True, args= ['--no-sandbox'] )
    page = await browser.newPage()
    await page.goto('https://coolors.co/generate',{'waitUntil' : 'networkidle2'})
    js = "() => { return window.location.href }"
    result = await page.evaluate(js)
    await browser.close()

    return result