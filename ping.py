"""
A Ping represents a vehicle's position at a given timestamp.
"""

from position import Position


class Ping(object):

    def __init__(self, x, y, timestamp):
        self.position = Position(x, y)
        # Timestamp of the ping, in seconds since the epoch.
        self.timestamp = timestamp

    def get_position(self):
        return self.position

    def get_timestamp(self):
        # timestamp in seconds since a fixed (but arbitrary) epoch.
        return self.timestamp

    def __str__(self):
        # dunder string method.
        return (str(self.position) + " @ " + str(self.timestamp))


def seconds_between(ping1, ping2):
    """
    Determines the number of seconds between two given Pings. The result is
    positive if ping1 is earlier than ping2.
    """
    return ping2.get_timestamp() - ping1.get_timestamp()
