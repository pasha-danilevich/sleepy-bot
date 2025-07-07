from entity.tracker.enums import SleepState


async def get_sleep_state(**kwargs) -> dict:
    sleep_state = SleepState.SLEEPING
    return {
        'is_awake': sleep_state == SleepState.AWAKE,
        'is_sleeping': sleep_state == SleepState.SLEEPING,
    }
