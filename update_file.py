#! /usr/bin/env python
"""
Update file on AWS S3 Bucket.

This module implements a mechanism to look out for file updates that
are automatically updated to an AWS S3 bucket.

"""

import os
import sys
from time import sleep, strftime, localtime
import subprocess


class FileChecker(object):
    """Implements a File checking object."""

    running = True

    def __init__(self, file_, delay_sec=1, *args, **kwargs):  # callback=None
        """Iniitalize the FileChecker."""
        self._ftstamp = 0
        self._filename = file_
        self._delay_sec = delay_sec
        self.args = args
        self.kwargs = kwargs

    def check(self):
        """Check if the file has changed based on time stamp."""
        stamp = os.stat(self._filename).st_mtime
        if stamp != self._ftstamp:
            self._ftstamp = stamp
            # print("\n{}".format(subprocess.check_call(
            #       ["aws", "s3", "ls", "s3://dm240bucket"])))
            try:
                subprocess.check_call(["aws", "s3", "cp", "./index.html",
                                       "s3://dm240bucket"])
                print("Updated file copied to S3 {}")
            except Exception as e:
                print("File not copied {}".format(e))

    def poll(self):
        """Poll and listen for changes on the given file."""
        print(">>> Polling...")
        while self.running:
            try:
                sleep(self._delay_sec)
                self.check()
            except KeyboardInterrupt:
                print("\n*****Program Exited*****\n")
                break
            except FileNotFoundError:
                print("*****The file is not found*****")
                break
            else:
                updated = strftime("%a, %d %b %Y %H:%M:%S", localtime())
                with open('index.html', 'a+') as f_:
                    f_.write('<br> Last Update: {}'.format(updated))
                # print("Unhandled Error".format(sys.exc_info()[0]))


if __name__ == '__main__':
    f = FileChecker('index.html', delay_sec=20)
    f.poll()
