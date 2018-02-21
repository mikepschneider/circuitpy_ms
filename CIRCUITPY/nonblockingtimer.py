import time

class NonBlockingTimer:

    def __init__(self):
        self.current_time = time.monotonic()
        self.last_time = self.current_time
        self.interval = 0.5

    def next(self):
        """ Do the next step of the timer, then if needed call set_interval() to
            determine how long this timer should yield (seconds) till the next
            step."""
        self.current_time = time.monotonic()
        elapsed = self.current_time - self.last_time
        if (elapsed > self.interval):
            # The timer has been "triggered"
            self.last_time = self.current_time
            return True
        return False

    def set_interval(self, seconds):
        self.interval = seconds

    def stop(self):
        """Stop the timer and do any cleanup needed."""
        pass
