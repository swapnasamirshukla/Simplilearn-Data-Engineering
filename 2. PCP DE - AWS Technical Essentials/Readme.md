# Monitoring EC2 Instance with AWS CloudWatch

## Description
Heaven Classics successfully created an EC2 Server Instance for Windows 2012 Server. After launching the instance, the next step was to monitor its operations. Monitoring is essential to keep an eye on the performance of an EC2 instance, gather data from all parts, and debug failures.

The monitoring team at Heaven Classics started using the CloudWatch Service in the AWS Management Console to monitor activities. The support team at Heaven Classics was required to meet the following objectives:

### Objectives

1. **Check and Observe the CPU Utilization Graph for the EC2 Instance**
   - Utilize CloudWatch to monitor the CPU utilization of the EC2 instance.

2. **Create and Configure a CloudWatch Alarm**
   - Set up a CloudWatch alarm that sends an email notification to HCMonitor@HeavenClassics.com if the CPU utilization goes below the threshold of 3%, consecutively three times for five minutes.

3. **Create an IAM Group Named Administrator Group**
   - Attach the full administrator access policy to the group.

4. **Create a User with Administrator Access**
   - Create a user for an employee of the company who requires administrator access to the company's AWS account.
   - Add the user to the Administrator Group.

### Steps to Perform

#### 1. Check and Observe the CPU Utilization Graph
- Navigate to the CloudWatch dashboard in the AWS Management Console.
- Select the EC2 instance and view the CPU utilization metric.

#### 2. Create and Configure a CloudWatch Alarm
- Go to the CloudWatch Alarms section.
- Create a new alarm and select the CPU utilization metric for the EC2 instance.
- Set the threshold to 3% and configure it to trigger an alarm if the threshold is breached three times in five minutes.
- Configure the alarm actions to send an email notification to HCMonitor@HeavenClassics.com.

#### 3. Create an IAM Group Named Administrator Group
- Navigate to the IAM section in the AWS Management Console.
- Create a new group named `Administrator Group`.
- Attach the `AdministratorAccess` policy to the group.

#### 4. Create a User with Administrator Access
- Create a new IAM user for the employee.
- Add the user to the `Administrator Group`.
- Provide the user with the necessary credentials and instructions for accessing the AWS account.

By following these steps, Heaven Classics will be able to effectively monitor their EC2 instance and ensure that key stakeholders are notified of any critical performance issues. Additionally, setting up proper IAM roles and users will help maintain secure and efficient access control within the AWS environment.
