from datetime import datetime, timedelta


class SleepUtils:
    @staticmethod
    def get_sleep_duration(bedtime: datetime, wakeup_time: datetime) -> timedelta:
        """
        Возвращает продолжительность сна как разницу между wakeup_time и bedtime.
        """
        return wakeup_time - bedtime

    @classmethod
    def format_timedelta(cls, delta: timedelta) -> str:
        """
        Принимает timedelta и возвращает строку вида:
        "X часов Y минут Z секунд" на русском, без лишних нулей.
        """
        total_seconds = int(delta.total_seconds())
        if total_seconds <= 0:
            return "0 секунд"

        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        parts = []
        if hours > 0:
            parts.append(f"{hours} {cls._pluralize(hours, 'час', 'часа', 'часов')}")
        if minutes > 0:
            parts.append(f"{minutes} {cls._pluralize(minutes, 'минута', 'минуты', 'минут')}")
        if seconds > 0:
            parts.append(
                f"{seconds} {cls._pluralize(seconds, 'секунда', 'секунды', 'секунд')}"
            )

        return " ".join(parts)

    @staticmethod
    def _pluralize(n: int, form1: str, form2: str, form5: str) -> str:
        """
        Склонение слов в русском языке для чисел.
        form1 - если n оканчивается на 1, кроме 11
        form2 - если n оканчивается на 2-4, кроме 12-14
        form5 - во всех остальных случаях
        """
        n = abs(n) % 100
        n1 = n % 10
        if 11 <= n <= 14:
            return form5
        if n1 == 1:
            return form1
        if 2 <= n1 <= 4:
            return form2
        return form5
