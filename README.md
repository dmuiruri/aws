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

The script could be extended to be more generic and listen to all file
in a folder that may require to be updated to the AWS cloud