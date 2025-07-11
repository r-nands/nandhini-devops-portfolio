# Terraform AWS S3 Static Website Hosting Project

This document outlines the process of deploying a static website on AWS S3 using Terraform, covering the project concept, file structure, resource definitions, and deployment steps.

## 1. Project Concept
The primary goal of this project is to host a static website on Amazon S3. This involves:

Automated Infrastructure Provisioning: Using Terraform to define and provision all necessary AWS resources (specifically an S3 bucket).

Website Content Deployment: Uploading the website's static files (e.g., index.html, error.html) directly to the S3 bucket using Terraform.

Public Accessibility: Configuring the S3 bucket for static website hosting and ensuring public read access to the website content.

## 2. Prerequisites
Before starting this project, ensure you have the following:

AWS Account: An active AWS account with appropriate permissions to create S3 buckets and manage their policies.

AWS CLI Configured: Your AWS credentials configured locally (e.g., via aws configure).

Terraform Installed: Terraform CLI installed on your local machine.

Website Content: Your static website files (at minimum index.html and error.html) ready in a local directory.

## 3. Project Structure
A typical project structure for this setup would look like this:

main.tf
variables.tf
provider.tf
outputs.tf
index.html
error.html

## 4. Deployment Steps

a.AWS Provider Configuration
b.Declare variables.tf
c.S3 Bucket Creation
d.S3 Bucket Ownership Controls
e.S3 Bucket Public Access Block
f.S3 Bucket ACL 
g.S3 Bucket Website Configuration
h.Uploading Website Files
i.Define output.tf

Once above files created, go to terminal and initialize terraform.

terraform init
terraform plan
terraform apply -auto-approve


## 5.Validation:
Now, s3 bucket will be created. Go to bucket and verify all your requirements are there(object, properites, permissions). Under properties you can find static website hosting, hit the URL and verify if you are getting the expected website.
