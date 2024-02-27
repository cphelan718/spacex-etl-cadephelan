# Technical Assessment



# Dependencies
import pandas as pd
import json
import requests
import openpyxl
import asyncio
import aiohttp
import pyarrow.parquet as pq
from prefect import task, flow



# test or EDA to understand contents of API
response = requests.get("https://api.spacexdata.com/v5/launches/latest")
response_json = json.loads(response.text)
response_json



# EXTRACT
async def extract_data():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.spacexdata.com/v5/launches/latest") as response:
            data = await response.json()
    return data



# TRANSFORM
async def process_data():
    processed_data = []
    return process_data

async def partition_data(process_data):
    return partition_data

async def to_parquet(partition_data):
    return to_parquet



# LOAD
async def load_data():
    pass