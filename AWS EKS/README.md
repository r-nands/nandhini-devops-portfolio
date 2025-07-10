EKS-Ingress Project Plan: Deploying 2048 Game on Amazon EKS with External Access

Project Overview:
This document outlines the plan for deploying a 2048 game application onto an Amazon Elastic Kubernetes Service (EKS) cluster. The primary objective is to host the game application in a highly scalable and resilient Kubernetes environment on AWS, and to provide external users with seamless access to the application via an AWS Application Load Balancer (ALB) managed by an Ingress Controller.

This project emphasizes a Command Line Interface (CLI)-driven deployment approach, leveraging eksctl, AWS CLI, kubectl, and Helm for automation and infrastructure as code principles, minimizing direct interaction with the AWS Management Console.

1.Key Technologies and Components:

The following AWS services and open-source tools are integral to this project:

Amazon Elastic Kubernetes Service (EKS): A managed Kubernetes service that simplifies the deployment, management, and scaling of containerized applications using Kubernetes on AWS.

AWS Fargate: A serverless compute engine for Amazon EKS that allows running containers without provisioning, managing, or scaling EC2 instances. This enhances operational simplicity and cost-effectiveness for application pods.

AWS Identity and Access Management (IAM): Used for securely managing access to AWS services and resources. Specifically, IAM Roles for Service Accounts (IRSA) will be utilized to grant Kubernetes service accounts fine-grained permissions to AWS resources.

AWS Application Load Balancer (ALB): A highly scalable and available load balancer that distributes incoming application traffic across multiple targets, such as Kubernetes pods.

AWS Load Balancer Controller: A Kubernetes controller that manages ALBs for an EKS cluster. It satisfies Kubernetes Ingress resources by provisioning ALBs, target groups, and listeners.

eksctl: A simple CLI tool for creating and managing Kubernetes clusters on Amazon EKS.

AWS Command Line Interface (CLI): A unified tool to manage AWS services from the command line.

kubectl: The command-line tool for running commands against Kubernetes clusters.

Helm: The package manager for Kubernetes, used to define, install, and upgrade even the most complex Kubernetes applications (like the AWS Load Balancer Controller).

2.Architectural Overview
The architecture for the 2048 game deployment will follow a standard pattern for containerized applications on EKS:

EKS Cluster: The core Kubernetes control plane managed by AWS.

Fargate Profiles: Application pods (including the 2048 game) will run on Fargate, abstracting away underlying EC2 instance management.

IAM Roles for Service Accounts (IRSA): A dedicated IAM role will be created and associated with a Kubernetes Service Account. This Service Account will be used by the AWS Load Balancer Controller to interact with AWS APIs (e.g., creating ALBs).

AWS Load Balancer Controller Deployment: The controller will be deployed within the EKS cluster, listening for Ingress resource definitions.

2048 Game Application: The game will be deployed as Kubernetes Deployments and Services.

Kubernetes Ingress: An Ingress resource will be defined for the 2048 game's Service. This Ingress resource will contain annotations that instruct the AWS Load Balancer Controller to provision an ALB and route external traffic to the game pods.

External Access: External users will access the 2048 game via the DNS name of the AWS ALB provisioned by the controller.

3. High-Level Deployment Steps (CLI-Driven)
The deployment process will involve the following sequence of operations, executed primarily via command-line tools:

Prerequisites Setup:

Ensure aws CLI, eksctl, kubectl, and helm are installed and configured on the local workstation.

EKS Cluster Creation: Use eksctl to create the EKS cluster, specifying Fargate profiles for application workloads.

IAM Policy for AWS Load Balancer Controller:Create a dedicated IAM policy (AWSLoadBalancerControllerIAMPolicy) with the necessary permissions for the ALB Controller to manage ALBs, target groups, and related resources.

IAM Service Account for AWS Load Balancer Controller:Create a Kubernetes Service Account (aws-load-balancer-controller) in the kube-system namespace and associate it with the newly created IAM policy using eksctl. This enables IRSA.

Install AWS Load Balancer Controller via Helm:Add the EKS Helm charts repository.Install the aws-load-balancer-controller Helm chart into the kube-system namespace, configuring it to use the pre-created Service Account and specifying the cluster name and image repository.

Deploy 2048 Game Application:Define Kubernetes manifests (Deployment, Service, Ingress) for the 2048 game.
The Ingress resource will include annotations to instruct the AWS Load Balancer Controller to provision an ALB and route traffic to the 2048 game service.

Verify Deployment and Access:Monitor the status of the AWS Load Balancer Controller pods.
Check for the creation of the ALB in the AWS console or via aws elb describe-load-balancers.
Retrieve the ALB DNS name from the Ingress resource using kubectl get ingress.
Access the 2048 game application via the ALB's DNS name in a web browser.

4. Benefits of This Approach
Scalability & High Availability: EKS and Fargate provide inherent scalability and high availability for the application.

Serverless Compute: Fargate eliminates the need to manage EC2 instances, reducing operational overhead and ensuring optimal resource utilization.

Automated Load Balancing: The AWS Load Balancer Controller automates the provisioning and management of ALBs, simplifying external access configuration.

Security: IAM Roles for Service Accounts (IRSA) ensure secure, fine-grained access for Kubernetes workloads to AWS resources.

Infrastructure as Code (IaC): The CLI-driven approach promotes IaC, allowing for repeatable, version-controlled deployments.

Cost-Effectiveness: Fargate's pay-per-use model for compute resources can be more cost-effective than managing dedicated EC2 instances, especially for fluctuating workloads.
