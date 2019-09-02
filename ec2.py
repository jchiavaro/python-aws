import boto3
import argparse


class EC2:
    def __init__(self):
        self.ec2 = boto3.client('ec2')

    def create_instance(self):
        resp = self.ec2.run_instances(
            ImageId='ami-0b898040803850657',
            InstanceType='t1.micro',
            MaxCount=1,
            MinCount=1
        )

        return resp

    def stop_instance(self, instance_id):
        response = self.ec2.stop_instances(
            InstanceIds=[instance_id]
        )

    def start_instance(self, instance_id):
        response = self.ec2.start_instances(
            InstanceIds=[instance_id]
        )

    def terminate_instance(self, instance_id):
        response = self.ec2.terminate_instances(
            InstanceIds=[instance_id]
        )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--create", help="Create a new ec2 instance",
                        action="store_true")
    parser.add_argument("--stop", help="Stop an instance",
                        action="store_true")
    parser.add_argument("--start", help="Start an instance",
                        action="store_true")
    parser.add_argument("--terminate", help="Terminate an instance",
                        action="store_true")
    parser.add_argument("--instance-id", help="The instance id",
                        type=str)
    args = parser.parse_args()
    ec2 = EC2()
    try:
        if args.create:
            response = ec2.create_instance()
            print("instance creted!")
        elif args.stop:
            ec2.stop_instance(args.instance_id)
            print("instance stopped")
        elif args.start:
            ec2.start_instance(args.instance_id)
            print("instance stopped")
        elif args.terminate:
            ec2.terminate_instance(args.instance_id)
            print("instance terminated")
        else:
            print("Invalid option")
    except Exception as e:
        print(repr(e))
