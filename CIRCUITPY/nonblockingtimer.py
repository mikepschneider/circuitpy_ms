import time

class NonBlockingTimer:


    def __init__(self, interval = -1):
        """interval < 0 == OFF (default) """
        self._interval = interval
        self._current_time = time.monotonic()
        self._last_time = self._current_time
        self._stopped = False

    def next(self):
        """ Return true if the timer has been 'triggered' else
            false.  If interval < = return false """

        if self._interval < 0:
            return False

        self._current_time = time.monotonic()
        elapsed = self._current_time - self._last_time

        if (elapsed > self._interval):
            # The timer has been "triggered"
            self._last_time = self._current_time
            return True
        return False

    def set_interval(self, seconds):
        """ Set the trigger interval time """
        if (self._interval < 0 and seconds >= 0):
            self.start()
        self._interval = seconds

    def start(self):
        print("NonBlockingTimer.start")

    def stop(self):
        """Stop the timer and do any cleanup needed. Restart by setting
        interval >= 0."""
        self._interval = -1
