#!/usr/bin/env python
# encoding: utf-8

import asyncio


loop =asyncio.get_event_loop()

async def take_exam(fut):
    await asyncio.sleep(1)
    fut.set_result(100)
    return 'Exam is completed.'

def check_score(fut):
    score = fut.result()
    if score >= 60:
        print('Passed.')
    else:
        print('Failed.')


fut = asyncio.Future()
fut.add_done_callback(check_score)    # 添加回调函数
task = asyncio.ensure_future(take_exam(fut))    # 把take_exam()封装成task
retval = loop.run_until_complete(fut)    # 可以传递coroutine或future,这传的是future,得到的就是future的结果

print(task.result())
print(fut.result())
print(retval)
