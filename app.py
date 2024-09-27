from fastapi import FastAPI
from fastapi.responses import JSONResponse
import asyncpg
import os

app = FastAPI()

async def get_db_connection():
    conn = await asyncpg.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        port=os.getenv('DB_PORT', '5432'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS')
    )
    return conn

@app.get('/data')
async def get_data():
    conn = await get_db_connection()
    data = await conn.fetch('SELECT * FROM dummy_data')
    await conn.close()
    return JSONResponse(content=[dict(record) for record in data])

@app.get('/health')
async def health():
    return {"status": "ok"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=5000)
