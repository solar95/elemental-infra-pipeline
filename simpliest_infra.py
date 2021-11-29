from diagrams.aws.devtools import Codecommit, Codebuild, Codepipeline
from diagrams.aws.management import Cloudwatch
from diagrams.aws.storage import SimpleStorageServiceS3Bucket
from diagrams.onprem.client import User
from diagrams import Cluster, Diagram, Edge

with Diagram("Infrastructure Pipeline", show=True):
    source = Codecommit("Infra Repo")
    developer = User("Developer")
    with Cluster(""):
        codepipeline = Codepipeline("Codepipeline \nSource Stage") 
        manual_approve = Codepipeline("Codepipeline \nMannual Approval") 
        cb_planner = Codebuild("Codebuild \nTerraform Plan")
        cb_deployer = Codebuild("Codebuild \nTerraform Apply")
        developer >> source >> Edge(label="Trigger") >> codepipeline >> cb_planner >> manual_approve>> cb_deployer
    