#!/bin/bash

# Put sensitive info here, which doesn't get imported into github
source ./secrets.bash

BUILD_DIR=${CWD};
ARLODASHBUTTON_VIRTUALENV="~/.virtualenvs/arlolambda";

echo "Rebuilding Deployment Package...";

cd ${ARLODASHBUTTON_VIRTUALENV}/lib/python2.7/site-packages
zip -r9 ${BUILD_DIR}/ArloDashButton.zip *
cd ${BUILD_DIR};
zip -g ArloDashButton.zip ArloDashButton.py

echo "Pushing to AWS...";

aws lambda delete-function --function-name ArloDashButton;
	
aws lambda create-function \
--region us-east-1 \
--function-name ArloDashButton \
--zip-file fileb://./ArloDashButton.zip \
--role ${AWS_ROLE} \
--environment Variables="{USERNAME=${ARLO_USERNAME},PASSWORD=${ARLO_PASSWORD},PRIMARY_CONTACT=${PRIMARY_CONTACT},SECONDARY_CONTACT=${SECONDARY_CONTACT}}"
--handler ArloDashButton.lambda_handler \
--runtime python2.7 \
--timeout 10 \
--memory-size 1024;

