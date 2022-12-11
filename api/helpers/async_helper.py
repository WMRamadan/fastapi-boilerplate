"""This module is the helper for all async operations."""
#--------------------------------------------#
# PEP-8 Imports Priority.
# 1.Standard Library Imports
# 2.Related Library Imports
# 3.Local application/library imports
#--------------------------------------------#
import asyncio


async def async_func_a(exec_time: int):
    """
    Asynchronous function a
    :param exec_time: Execution time in seconds.
    """
    await asyncio.sleep(exec_time)
    return f"Result returned in {exec_time} seconds!"

async def async_func_b(exec_time: int):
    """
    Asynchronous function a
    :param exec_time: Execution time in seconds.
    """
    await asyncio.sleep(exec_time)
    return f"Result returned in {exec_time} seconds!"
