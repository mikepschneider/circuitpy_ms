import time

class NonBlockingTimer:

    def __init__(self, interval):
        self._interval = interval
        self._current_time = time.monotonic()
        self._last_time = self._current_time
        self._stopped = False

    def next(self):
        """ Return true if the timer has been 'triggered' else
            false. """
        self._current_time = time.monotonic()
        elapsed = self._current_time - self._last_time

        if (self._stopped):
            return False

        if (elapsed > self._interval):
            # The timer has been "triggered"
            self._last_time = self._current_time
            return True
        return False

    def set_interval(self, seconds):
        """ Set the trigger interval time """
        self._interval = seconds

    def stop(self):
        """Stop the timer and do any cleanup needed. Once called
        the time can't be restarted. """
        self._stopped = True
