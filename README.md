# Overview

This module implements a mechanisim to update the index file as soon
as it changes as it is edited and saved, -tracking the file's
timestamp. Currently the approach implemented uses polling and
specifically listens to changes in the index file and run an AWS CLI
command to update the file in the S3 bucket. 

AWS command: `aws s3 cp file.html s3://bucket`

For the aws command to work, the proper credentials would need to be
setup at `~/.aws/credentials`

To run this file, the index.html file needs to be in the folder where
the script is running from.

The script could be extended to be more generic and listen to all files
in a folder that may require to be updated to the AWS cloud.

Notably, such a script can be used to complement AWS S3 bucket's
lifecycle feature if needed. The life cycle feature can be configured
to transition objects or files between various storage classes,
typically optimizing costs based on how often a file is accessed or
read. Amazon offers storage tiers that have 99.5% availability which
would be cheaper than those with 99.999% availability although they
still promise to offer low latency and high accessibility for these
files. At the very end of a file's life cycle, it could go into an
archive class.