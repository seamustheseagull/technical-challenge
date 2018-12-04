# Create and spinning up a solution using AWS ElasticBeanstalk

## Description

The configuration files in this solution allow you to stand up an minimally-functional ElasticBeanstalk environment incorporating an elastic load balancer supporting up to four instances, which will autoscale based on the current latency.

The solution runs on port 80 with a hacked-together homepage to validate node health

## Prereqs

This requires that you have the ElasticBeanstalk CLI installed on your machine;

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install-linux.html


## Steps to run using the EB CLI

- Clone/Download the repo to your machine

- Open a console and change to the `app` directory of the solution

- Initialise your elastic beanstalk local environment: `eb init` 
-- The access ID and Key should have appropriate roles/permission to spin up environments in AWS
-- Ensure you select Python 2.7 as the appropriate python version

- In the AWS console you will now see the application created

- Run the command `eb create tech-challenge-env` to create a new environment and deploy to EB

- After a few minutes the environment will be complete and accessible from the auto-generate URL specified in the ElasticBeanstalk console.
