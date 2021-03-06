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

    def __init__(self, path='.', delay_sec=5):
        """Iniitalize the FileChecker."""
        self._ftstamp = 0
        self._path = path
        self._files = {}
        self._uploadfiles = []
        self._delay_sec = delay_sec

    def folderscanner(self):
        """Get current time stamps."""
        ignored_dirs = ('__pycache__', '.git')
        for p, dirs, fs in os.walk(self._path):
            for d in ignored_dirs:
                if d in dirs:
                    dirs.remove(d)
            for fn in fs:
                fp = '{}/{}'.format(p, fn)
                self._files[fp] = os.stat(fp).st_mtime

    def uploader(self):
        """Upload files to an AWS S3 bucket."""
        for file in self._uploadfiles:
            try:
                subprocess.check_call(["aws", "s3", "cp", file,
                                       "s3://dm240bucket"])
                self._uploadfiles.remove(file)
            except Exception as e:
                print("File not copied {}".format(e))
                raise

    def check(self):
        """Check if the file has changed based on time stamp."""
        for key in self._files:
            stamp = os.stat(key).st_mtime
            if stamp != self._files[key]:
                self._uploadfiles.append(key)
                self._files[key] = stamp
        self.uploader()

    def poll(self):
        """Poll and listen for changes on the given file."""
        print(">>> Polling...")
        self.folderscanner()
        while self.running:
            try:
                sleep(self._delay_sec)
                self.check()
                print('{}\n'.format(self._files))
            except KeyboardInterrupt:
                print("\n*****Program Exited*****\n")
                break
            except FileNotFoundError:
                print("*****The file is not found*****")
                break
            else:
                print('{}'.format(self._uploadfiles))
                # updated = strftime("%a, %d %b %Y %H:%M:%S", localtime())
                # with open('index.html', 'a+') as f_:
                #     f_.write('<br> Last Update: {}'.format(updated))
                # print("Unhandled Error".format(sys.exc_info()[0]))


if __name__ == '__main__':
    f = FileChecker(path='.', delay_sec=6)
    f.poll()
