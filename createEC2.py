# import boto3

# ec2=boto3.client('ec2')


# image_id="ami-05fa46471b02db0ce"
# instance_type="t2.micro"
# key_name="my_ec2"

# response = ec2.run_instances(
#     ImageId=image_id,
#     InstanceType=instance_type,
#     KeyName=key_name,  # Ensure this key exists in your AWS account
#     MinCount=1,
#     MaxCount=1
# )
# print(response)