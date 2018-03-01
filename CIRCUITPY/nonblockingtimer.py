import time

class NonBlockingTimer:

    def __init__(self, interval = 0.5):
        self._interval = interval
        self._current_time = time.monotonic()
        self._last_time = self._current_time

    def next(self):
        """ Return true if the timer has been 'triggered' else
            false. """
        self._current_time = time.monotonic()
        elapsed = self._current_time - self._last_time
        if (elapsed > self._interval):
            # The timer has been "triggered"
            self._last_time = self._current_time
            return True
        return False

    def set_interval(self, seconds):
        """ Set the trigger interval time """
        self._interval = seconds

    def stop(self):
        """Stop the timer and do any cleanup needed."""
        pass
