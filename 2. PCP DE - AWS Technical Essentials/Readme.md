# Monitoring EC2 Instance with AWS CloudWatch

## Description

Heaven Classics successfully creates an EC2 Server Instance for Windows 2012 Server. After launching the instance on the server, the next step was to monitor the operations. Monitoring is important to keep an eye on the performance of an EC2 instance. It helps gather data from all parts and is useful for debugging failure. The monitoring team at Heaven Classics started monitoring activities using the CloudWatch Service in the AWS Management Console. The Heaven Classics support team were required to meet the following objectives:

### Objectives

1. **Check and observe the CPU utilization graph for the EC2 instance**

2. **Create and configure a CloudWatch alarm that sends an email notification to HCMonitor@HeavenClassics.com if the CPU utilization goes below the threshold of 3%, consecutively three times for five minutes**

3. **Create an IAM group named Administrator Group and attach the full administrator access policy to the group**

4. **Create a user for an employee of the company who requires administrator access to the company's AWS account, and then add the user to the Administrator Group**
