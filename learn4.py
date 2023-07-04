import asyncio
import aiohttp
from aiohttp import ClientSession
from utils import async_timed
 
 
#@async_timed()
async def fetch_status(session: ClientSession, url: str, delay=0) -> int:
    await asyncio.sleep(delay)
    async with session.get(url) as result:
       #the below shows how to wait for the response tex
        status, text=result.status, await result.text()
        #await save_data(text)
        return status,text
 
  
@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://beta.clinicaltrials.gov/api/v2/studies?query.cond=&query.intr=&query.term=&fields=NCTId,BriefTitle,LeadSponsorName,LocationCity,LocationFacility,InterventionName,PrimaryOutcomeMeasure,BriefSummary,OverallStatus,Phase,Sex,EligibilityCriteria&countTotal=true&pageSize=5&'
        #url="https://www.example.com"
        fetchers = [asyncio.create_task(fetch_status(session, url)),
                    asyncio.create_task(fetch_status(session, url,  delay=0)),
                    asyncio.create_task(fetch_status(session, url, delay=0))]
 
        done, pending = await asyncio.wait(fetchers, timeout=1)
 
        print(f'Done task count: {len(done)}')
        print(f'Pending task count: {len(pending)}')
        for done_task in done:
            status, text=await done_task
            print(status, text)


#write a function that saves data to a .html file
async def save_data(text=""):
    with open("data.html", "w", encoding="utf-8") as f:
        f.write(text)   

asyncio.run(main()) 
 
