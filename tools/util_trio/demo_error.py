import trio


async def risky_task(task_id, should_fail=False):
    await trio.sleep(1)

    if should_fail:
        raise ValueError(f'Task {task_id} failed！')

    return f'Task {task_id} completed successfully'


async def error_handling_demo():
    try:
        async with trio.open_nursery() as nursery:
            nursery.start_soon(risky_task, 1, False)
            nursery.start_soon(risky_task, 2, True)  # 这个会失败
            nursery.start_soon(risky_task, 3, False)
    except Exception as e:
        # 当task 2失败时 其他所有任务都会被取消
        print(f'捕获到异常： {e}')
