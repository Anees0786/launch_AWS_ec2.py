

import boto3

def launch_ec2_instance():
    region_name = 'ap-south-1'
    instance_type = 't2.micro'
    image_id = 'ami-0ded8326293d3201b'
    
    ec2 = boto3.client('ec2', region_name=region_name)

    response = ec2.run_instances(
        ImageId=image_id,
        InstanceType=instance_type,
        MaxCount=1,
        MinCount=1,
    )

    return response

if __name__ == "__main__":
    print("Below is your Response")
    response = launch_ec2_instance()
    print(response)
