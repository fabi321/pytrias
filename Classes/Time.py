from Classes.StopWithoutLine import StopWithoutLine
import datetime
import time


def unix_time_from_time_string(time_string: str) -> int:
    time_string: str = time_string.replace('Z', '+00:00')
    try:
        time: datetime.datetime = datetime.datetime.fromisoformat(time_string)
    except AttributeError:
        time: datetime.datetime = datetime.datetime.strptime(time_string, "%Y-%m-%dT%H:%M:%S+00:00")
    return int(time.timestamp())
        


class Time:
    def __init__(self, stop: StopWithoutLine, est_time: str, plan_time: str, section: str):
        self._stop: StopWithoutLine = stop
        self._section: str = section
        self._estimated: int = unix_time_from_time_string(est_time)
        self._planned: int = unix_time_from_time_string(plan_time)

    def get_difference(self) -> int:
        return self._estimated - self._planned

    def get_estimated(self) -> int:
        return self._estimated

    def get_planned(self) -> int:
        return self._planned

    def get_section_id(self) -> str:
        return self._section

    def override(self, other):
        if not isinstance(other, Time):
            raise NotImplementedError('Tried to override Times with ' + str(type(other)))
        self = other

    def __str__(self) -> str:
        return str(self._stop)

    def __eq__(self, other) -> bool:
        if not isinstance(other, (Time, str)):
            raise NotImplementedError('Tried to compare Times with ' + str(type(other)))
        return self.__str__() == str(other)

    def __add__(self, other):
        if not isinstance(other, Time):
            raise NotImplementedError('Tried to add Times with ' + str(type(other)))
        if self != other:
            raise NotImplementedError('Tried to merge ' + self.__str__() + ' with ' + str(other))
        self._planned = other.get_planned()
        self._estimated = other.get_estimated()
        other.override(self)
        return self
