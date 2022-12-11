"""This module is for the async router."""
#--------------------------------------------#
# PEP-8 Imports Priority.
# 1.Standard Library Imports
# 2.Related Library Imports
# 3.Local application/library imports
#--------------------------------------------#
import time
import asyncio
from fastapi import APIRouter
from api.helpers import async_helper


router = APIRouter()

@router.get("/async")
async def root():
    """
    Async router.
    """
    start = time.time()
    async_a, async_b = await asyncio.gather(*[async_helper.async_func_a(2), async_helper.async_func_b(4)])
    end = time.time()
    result = {
        "async_func_a": async_a,
        "async_func_b": async_b,
        "async_total_time": "All functions took {} seconds.".format(round(end-start))
    }
    return result
