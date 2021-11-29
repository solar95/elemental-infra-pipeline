from diagrams.aws.devtools import Codecommit, Codebuild, Codepipeline
from diagrams.aws.management import Cloudwatch
from diagrams.aws.storage import SimpleStorageServiceS3Bucket
from diagrams.onprem.client import User
from diagrams import Cluster, Diagram, Edge

with Diagram("Infrastructure Pipeline", show=True, outformat="png", filename="mydemo"):
    source = Codecommit("Infra Repo")
    developer = User("Developer")
    
    with Cluster("AWS", direction="BT"):
        codepipeline = Codepipeline("Codepipeline \nSource Stage") 
        manual_approve = Codepipeline("Codepipeline \nMannual Approval") 
        cb_planner = Codebuild("Codebuild \nTerraform Plan")
        cb_deployer = Codebuild("Codebuild \nTerraform Apply")
        s3_artifacts = SimpleStorageServiceS3Bucket("S3 Artifacts \nBucket")
        cb_deployer << Edge( style="dotted") << s3_artifacts
        developer >> Edge(label="Push\nTerraform code")>> source >> Edge(label="Trigger") >> codepipeline >> cb_planner 
        cb_planner >> manual_approve
        cb_planner >>  Edge( style="dotted") >>s3_artifacts
        manual_approve  >> cb_deployer
        
        cw_logs = Cloudwatch("Cloudwatch\nLogs")

        # cb_deployer >> Edge(color="blue", style="dotted", label="Get\nterraform\nplan") >> s3_artifacts



        