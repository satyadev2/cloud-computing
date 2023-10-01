import boto3
cloudfront_client = boto3.client("cloudfront", region_name="ap-south-1")

cloudfront_client.create_distribution(
    DistributionConfig={
        "CallerReference": "09-09-2023",
        'Origins': {
            'Quantity': 1,
            'Items': [
                {
                    'Id': 'quantumsynergy',
                    'DomainName': 'lab2023iiitg.s3.ap-south-1.amazonaws.com',
                    'S3OriginConfig': {
                        'OriginAccessIdentity': ''
                    },
                },
            ]
        },
        'DefaultCacheBehavior': {
            'TargetOriginId': 'quantumsynergy',
            'ViewerProtocolPolicy': 'allow-all',
            'ForwardedValues': {
                'QueryString': False,
                'Cookies': {
                    'Forward': 'all',
                },
                'Headers': {
                    'Quantity': 0,
                },
                'QueryStringCacheKeys': {
                    'Quantity': 0,
                }
            },
            'MinTTL': 1000,
        },
        "Enabled": True,
        "Comment": "distribution to host portfolio",
    }
)
print("Environment successfully created")