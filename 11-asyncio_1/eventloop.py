#!/usr/bin/env python
# encoding: utf-8

import asyncio
import uvloop


async def compute(x, y):
    print('Compute %s + %s ...' % (x, y))
    await asyncio.sleep(1.0)
    return x + y

async def print_sum(x, y):
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))


loop = asyncio.get_event_loop()
print(loop)    # <_UnixSelectorEventLoop running=False closed=False debug=False>
loop.run_until_complete(print_sum(1, 2))
loop.close()


policy = uvloop.EventLoopPolicy()
asyncio.set_event_loop_policy(policy)
loop = asyncio.get_event_loop()
print(loop)    # <uvloop.Loop running=False closed=False debug=False>
loop.create_task(print_sum(3, 4))
#loop.run_forever()
#loop.stop()    # 一直在等待

new_loop = asyncio.new_event_loop()
print(new_loop)    # <uvloop.Loop running=False closed=False debug=False>
new_loop.create_task(print_sum(5, 6))
new_loop.stop()
new_loop.run_forever()    # 结果只有：Compute 5 + 6 ...
