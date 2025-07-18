* GitHub Actions CI/CD Tutorial Project Document
This document summarizes the key aspects and steps involved in setting up a Continuous Integration/Continuous Delivery (CI/CD) pipeline using GitHub Actions The project focuses on building a robust CI/CD workflow from scratch, integrating various development and security tools, and deploying an application to Kubernetes.

** 1. Project Overview
The primary goal of this project is to provide a comprehensive understanding of GitHub Actions by implementing a live CI/CD pipeline. It covers everything from repository setup to deploying an application, emphasizing the process of writing CI/CD YAML files from the ground up rather than relying solely on templates.

** 2. Key Concepts
	• GitHub Actions: A CI/CD platform provided by GitHub that allows you to automate your software development workflows directly within your GitHub repository. Workflows are defined using YAML files (.yml) and are triggered by events (e.g., push, pull_request).
	• CI/CD (Continuous Integration/Continuous Delivery):
		○ Continuous Integration (CI): Automates the process of merging code changes from multiple developers into a single main branch. It involves automated builds and tests to detect integration issues early.
		○ Continuous Delivery (CD): Automates the delivery of new code to various environments (e.g., staging, production) after the CI process is successful.
	• Runners: Virtual machines or containers where your GitHub Actions workflows execute.
		○ Shared Runners: Provided and managed by GitHub. They are free for public repositories and offer a convenient way to run jobs without managing infrastructure. However, they provide limited backend access.
		○ Self-Hosted Runners: Virtual machines or physical servers that you manage and host. They offer complete control over the environment, allowing for custom tool installations, specific hardware configurations, and enhanced isolation, though they incur infrastructure costs.

** 3. Tools and Technologies Utilized
The CI/CD pipeline integrates various tools to cover different aspects of the software development lifecycle:
	• Git/GitHub: Version control and hosting for the project repository.
	• Maven: Build automation tool for Java projects.
	• Trivy: A comprehensive security scanner for vulnerabilities in container images, file systems, and more.
	• GitLeaks: A tool to detect sensitive data (e.g., API tokens, secret keys) hardcoded in source code.
	• Docker: Platform for developing, shipping, and running applications in containers.
	• Kubernetes: An open-source container orchestration system for automating deployment, scaling, and management of containerized applications.
	• SonarQube (mentioned): A tool for continuous inspection of code quality to perform static code analysis.

** 4. CI/CD Pipeline Stages
The tutorial demonstrates building a multi-stage CI/CD pipeline with the following phases:
	1. Git Repository Setup: Initializing a new GitHub repository and pushing the project code.
	2. VM as Runner Setup: Configuring a virtual machine to act as a self-hosted runner for GitHub Actions.
	3. CI/CD Pipeline Definition (YAML): Writing the workflow file (.github/workflows/cicd.yml) to define the jobs and steps.
		○ Security Checks:
			§ Trivy File System Scan: Scans the project's file system for vulnerabilities.
			§ GitLeaks Code Scan: Detects hardcoded sensitive information in the source code.
		○ Test Cases: Executes unit tests for the application.
		○ Build Application & Publish Artifact: Compiles the source code and creates a deployable artifact.
		○ Build & Scan Docker Image: Builds a Docker image of the application and scans it for vulnerabilities.
		○ Push to Docker Registry: Pushes the built Docker image to a specified Docker registry.
		○ Deploy to Kubernetes Cluster: Deploys the application to a Kubernetes cluster.

** 5. Setting Up the Environment
5.1. GitHub Repository Setup
	1. Create a New Repository
	2. Clone the Repository
	3. Add Project Code
	4. Commit and Push
	
5.2. Using a Shared Runner (Initial Test)
	1. Navigate to the "Actions" tab in your GitHub repository.
	2. Select a template (e.g., "Java with Maven") or start a new workflow.
	3. A main.yml (or cicd.yml) file will be created in .github/workflows/.
	4. The runs-on: ubuntu-latest specifies the use of a shared Ubuntu runner.
	5. Commit the file to trigger the pipeline and observe its execution.
       
5.3. Setting up a Self-Hosted Runner
	1. Provision a Virtual Machine (VM): Create a Linux VM (e.g., Ubuntu 20.04/22.04 LTS) on your preferred cloud provider (e.g., AWS EC2). Ensure necessary security group ports are open.
	2. Connect to VM: SSH into your VM.
	3. Install Dependencies (e.g., Maven):
	4. Add Self-Hosted Runner to GitHub:
		○ In your GitHub repository, go to Settings > Actions > Runners.
		○ Click New self-hosted runner.
		○ Select your OS (e.g., Linux) and architecture.
		○ Follow the on-screen instructions to download, configure, and run the runner agent on your VM.
			§ Create a directory: mkdir actions-runner && cd actions-runner
			§ Download the runner package: curl -o actions-runner-linux-x64-<version>.tar.gz -L <download_url>
			§ Extract the package: tar xzf ./actions-runner-linux-x64-<version>.tar.gz
			§ Configure the runner (provide repository URL and token): ./config.sh
				□ When prompted for "Labels", enter self-hosted (or any custom label).
			§ Start the runner: ./run.sh (This command keeps the runner online and listening for jobs).

** 6. Create YAML Pipeline 
	• name: The name of your workflow.
	• on: Defines the events that trigger the workflow (e.g., push to a specific branch).
	• jobs: Contains one or more jobs.
		○ Each job runs in an isolated environment.
		○ runs-on: Specifies the runner environment (e.g., ubuntu-latest for shared, self-hosted for your VM).
		○ needs: Defines dependencies between jobs, ensuring they run in a specific order.
		○ steps: A sequence of tasks within a job.
			§ uses: Executes a predefined action (reusable units of code).
			§ name: A descriptive name for the step.
			§ run: Executes shell commands directly on the runner. Multi-line commands use |.

** 7. Conclusion
This project demonstrates how to effectively leverage GitHub Actions for building a comprehensive CI/CD pipeline. By understanding the concepts of shared and self-hosted runners, defining workflow stages, and integrating various development and security tools, you can automate your software delivery process, ensuring faster, more reliable, and secure deployments.
<img width="1140" height="2204" alt="image" src="https://github.com/user-attachments/assets/ef991700-fbbd-4381-b01b-3ab960b3c6e5" />
