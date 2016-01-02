#/bin/bash

commit=`git rev-parse HEAD | cut -c 1-7`
environment=$1

if [ -z "$environment" ]; then
  echo "Example usage: deploy.sh <environment>";
  exit 1
fi

echo "Deploying commit $commit to $environment"
eb deploy $environment -l $commit
