# Overview

Files in this folder are lambda functions that are uploaded to the
lambda server in aws.

Using the aws cli, it is more convenient to edit the files locally
then upload them to aws. The functions are uploaded in a zip file -I
assume it should be possible to have the functions stated in one file
and packaged in one zip file but referenced differently during the
function creation command

##### Create a zip file:
`zip removetask.zip ./removetask.py`

##### Create a function:

`aws lambda create-function --function-name removetask --zip-file fileb://removetask.zip --handler removetask.removeTask_handler --runtime python3.7 --role arn:aws:iam::[-------------]:role/dmlambda`

The `--handler` option takes a <file>.<function> python syntax, which
is the reason I think it should be possible to have all the functions
in one file and dereferenced by changing the function name attribute.

##### Updating a created function:
`aws lambda update-function-code --function-name removetask --zip-file fileb://removetask.zip`