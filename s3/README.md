# Overview

This module contains a simple static files (index.html) that forms the
application's UI.

# Automating Backup Using AWS S3

This module implements a mechanisim to backup a given folder to an AWS
bucket as soon as the contents change i.e as files are being edited
and saved. This module achieves that functionality by tracking a
file's timestamps. Currently the approach implemented uses polling and
specifically listens to changes in the files and when changes are
detected an AWS CLI command to update the file in the S3 bucket is
issued.

AWS command: `aws s3 cp file.html s3://bucket`

For the aws command to work, the proper credentials would need to be
setup at `~/.aws/credentials` and this script would need to be running
in the background when editing of files is ongoing.

Notably, such a script can be used to complement AWS S3 bucket's
lifecycle feature if needed. The life cycle feature can be configured
to transition objects or files between various [storage
classes](https://aws.amazon.com/s3/storage-classes/). Typically
optimizing costs based on how often a file is accessed or read. Amazon
offers storage tiers that have 99.5% availability which would be
cheaper than those with 99.999% availability although they still
promise to offer low latency and high accessibility for these
files. At the very end of a file's life cycle, it could go into an
archive class.

## Design Observations

The approach taken in this script is to check whether a file has been
modified by looking at the *Time of most recent content modification
expressed in seconds.*

In Python

```python
import os

mtime = os.stat(filepath).st_mtime
```

If a file is saved (save icon or key press) the metadata is changed to
show that the file has been modified even though no new content has
been added or removed. This can either be a desirable feature or cause
unnecessary bandwidth consumption in a large deployment. Perhaps a
more elegent solution would be to have some system timers that would
fireup when and if a file changes instead of a busy loop.

PS: A typical usecase where automating backup may be required is when
hosting static websites. To access a public bucket's endpoint(domain
name) for example when used for website hosting, the domain name can
be found from the buckets "Properties => Static Web hosting" tab, more
details can be found
[here](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html).

AWS cli commands to work with S3 can be found
[here](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html).