import boto3

client = boto3.client("elasticbeanstalk")


client.create_application_version(
        ApplicationName="quantum_synergy",
    AutoCreateApplication=True,
    Description="kush_satyadev",
    Process=True,
    SourceBundle={
        "S3Bucket": "lab2023iiitg",
        "S3Key": "Portfolio.zip",
    },
    VersionLabel="v1",
)

import time

while True:

    response = client.describe_application_versions(
        ApplicationName="quantum_synergy",
        VersionLabels=[
            "v1",
        ],
        MaxRecords=1,
    )

    if response["ApplicationVersions"][0]["Status"] != "PROCESSED":
        print("Creating Application")
        time.sleep(5)
    else:
        print("Application Created Successfully")
        break
    

response = client.create_environment(
    ApplicationName="quantum_synergy",
    CNAMEPrefix="satyaa",
    EnvironmentName="quantum-env",
    SolutionStackName="64bit Amazon Linux 2 v5.8.5 running Node.js 18",
    VersionLabel="v1",
    OptionSettings=[
        {
            "Namespace": "aws:autoscaling:launchconfiguration",
            "OptionName": "IamInstanceProfile",
            "Value": "portfolio-access",
        },
        {
            "Namespace": "aws:autoscaling:launchconfiguration",
            "OptionName": "InstanceType",
            "Value": "t2.micro",
        },
        {
            "Namespace": "aws:autoscaling:launchconfiguration",
            "OptionName": "EC2KeyName",
            "Value": "kush_satyadev",
        },
        {
            "Namespace": "aws:autoscaling:launchconfiguration",
            "OptionName": "ImageId",
            "Value": "ami-097e7acc1d0c8b1b9",
        },
        {
            "Namespace": "aws:autoscaling:launchconfiguration",
            "OptionName": "SecurityGroups",
            "Value": "sg-036d12829b059381a",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "Statistic",
            "Value": "Average",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "Period",
            "Value": "1",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "UpperThreshold",
            "Value": "80",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "UpperBreachScaleIncrement",
            "Value": "1",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "MeasureName",
            "Value": "CPUUtilization",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "LowerThreshold",
            "Value": "20",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "LowerBreachScaleIncrement",
            "Value": "-1",
        },
        {
            "Namespace": "aws:autoscaling:asg",
            "OptionName": "Availability Zones",
            "Value": "Any 2",
        },
        {
            "Namespace": "aws:autoscaling:asg",
            "OptionName": "MaxSize",
            "Value": "3",
        },
        {
            "Namespace": "aws:autoscaling:asg",
            "OptionName": "MinSize",
            "Value": "1",
        },
        {
            "Namespace": "aws:ec2:vpc",
            "OptionName": "Subnets",
            "Value": "subnet-0fc56dd261b40b456 "
        },

    ],
)

print("Environment successfully created")


# IamInstanceProfile: Specifies the IAM instance profile for EC2 instances in the environment.

# InstanceType: Specifies the EC2 instance type to be used for the environment (e.g., t2.micro).

# EC2KeyName: Specifies the EC2 key pair to use for SSH access to instances.

# ImageId: Specifies the Amazon Machine Image (AMI) ID for EC2 instances.

# SecurityGroups: Specifies the security group to be associated with EC2 instances.

# Auto Scaling Configuration: Configures auto-scaling settings based on CPU utilization thresholds.

# Availability Zones: Specifies the availability zones where the environment can be launched.

# MinSize and MaxSize: Configures the minimum and maximum number of instances in the auto-scaling group.

# Subnets: Specifies the VPC subnets where the environment will be launched.