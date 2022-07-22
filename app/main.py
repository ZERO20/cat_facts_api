import datetime

import requests
import uvicorn
from fastapi import FastAPI, HTTPException

from app.config import Settings


settings = Settings()
app = FastAPI(
    debug=settings.DEBUG,
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION
)


@app.get("/health-check")
async def health_check():
    return {"status": "Running..."}


@app.get("/cat-facts/{number}")
async def cat_facts(number: int):
    if number > 500:
        raise HTTPException(status_code=400, detail="Maximum exceeded")
    size = total_size = number
    facts = {}
    current_year = str(datetime.datetime.today().year)
    while len(facts) < total_size:
        params = {
            'amount': size
        }
        r = requests.get(url='https://cat-fact.herokuapp.com/facts/random', params=params)
        r_json = r.json()
        result = [r_json] if isinstance(r_json, dict) else r_json
        facts_current_year = {
            cat['_id']: cat for cat in result if cat['updatedAt'][:4] == current_year and cat['_id'] not in facts}
        facts.update(facts_current_year)
        size -= len(facts_current_year)
    return list(facts.values())


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
