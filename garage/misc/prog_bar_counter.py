"""A progress bar counter class."""
import pyprind

from garage.misc import logger
from garage.misc.logger.logger_outputs import StdOutput


class ProgBarCounter:
    """Record progress in a bar counter format."""

    def __init__(self, total_count):
        """Init function."""
        self.total_count = total_count
        self.max_progress = 1000000
        self.cur_progress = 0
        self.cur_count = 0
        if logger.has_output(StdOutput):
            self.pbar = pyprind.ProgBar(self.max_progress)
        else:
            self.pbar = None

    def inc(self, increment):
        """Increment function."""
        if logger.has_output(StdOutput):
            self.cur_count += increment
            new_progress = (
                self.cur_count * self.max_progress / self.total_count)
            if new_progress < self.max_progress:
                self.pbar.update(new_progress - self.cur_progress)
            self.cur_progress = new_progress

    def stop(self):
        """Stop function."""
        if self.pbar is not None and self.pbar.active:
            self.pbar.stop()
