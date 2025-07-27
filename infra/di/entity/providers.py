from dishka import Provider, Scope, provide

from entity.tracker.repo import SleepRecordRepo
from entity.tracker.service import TrackerService
from entity.user.repo import UserRepo
from entity.user.service import UserService


class UserProvider(Provider):
    scope = Scope.APP

    service = provide(UserService)
    repo = provide(UserRepo)
    sr_repo = provide(SleepRecordRepo)
    tracker_service = provide(TrackerService)
