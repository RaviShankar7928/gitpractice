def lambda_handler(event, context):
    client = boot3.client('ec2')
    response = client.run_instance(
            ImageId='ami-0614680123427b75e',
            InstanceType='t2.micro',
            KeyName='mykeymumbai',
            MaxCount=2,
            MinCount=1
            )
    
