## Kubernetes Monitoring Setup: Prometheus, Grafana, and Kube-State-Metrics
This document details the process of deploying and configuring a robust monitoring solution on a Kubernetes cluster using Prometheus for metrics collection, Grafana for visualization, and Kube-State-Metrics for cluster-level insights. The deployment utilizes Helm charts for simplified management and Minikube as the local Kubernetes environment.

## 1. Prerequisites
Before starting, ensure you have the following tools installed and configured:

Minikube: A local Kubernetes environment. Your project uses the Docker driver.

Verify Minikube status: minikube status (should show host: Running, kubelet: Running)

kubectl: The Kubernetes command-line tool.

Verify connection: kubectl cluster-info

Helm 3: The Kubernetes package manager.

Verify installation: helm version

## 2. Setting Up Prometheus
Prometheus will be deployed to collect metrics from your Kubernetes cluster and its components.

2.1. Add Prometheus Community Helm Repository
DOS

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
2.2. Install Prometheus using Helm
This installs the Prometheus server, Alertmanager, Node Exporter, Kube-State-Metrics, and Pushgateway with default settings into the default namespace.

helm install prometheus prometheus-community/prometheus

2.3. Verify Prometheus Deployment

Check that all Prometheus-related pods are running.
kubectl get pods -n default


You should see pods like prometheus-server-XXXX, prometheus-alertmanager-0, prometheus-kube-state-metrics-XXXX, etc., with a Running status and healthy READY counts.

2.4. Access Prometheus Dashboard via Port Forwarding
To access the Prometheus UI from your local machine:

Open a NEW Command Prompt window.

Keep this window open during access.

Retrieve Prometheus Pod Name:

kubectl get pods --namespace default -l "app.kubernetes.io/name=prometheus,app.kubernetes.io/instance=prometheus" -o jsonpath="{.items[0].metadata.name}" > prometheus_pod_name.txt
set /p POD_NAME=<prometheus_pod_name.txt
del prometheus_pod_name.txt


Perform Port Forwarding:

kubectl --namespace default port-forward %POD_NAME% 9090:9090
Access in Browser:
Navigate to http://localhost:9090 in your web browser.

## 3. Setting Up Grafana
Grafana will be deployed to visualize the metrics collected by Prometheus.

3.1. Add Grafana Helm Repository

helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
3.2. Install Grafana using Helm
This installs Grafana with default settings into the default namespace.

helm install grafana grafana/grafana --namespace default
3.3. Retrieve Grafana Admin Password
Since the base64 command is not native to Windows CMD, use PowerShell to decode the password:

Open a PowerShell window.

Retrieve Encoded Password:


$GRAFANA_PASSWORD_ENCODED = kubectl get secret --namespace default grafana -o jsonpath="{.data.admin-password}"
Decode Password:

[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($GRAFANA_PASSWORD_ENCODED))
This will output your plain-text admin password. The username is admin.

3.4. Access Grafana Dashboard via Port Forwarding
Open a NEW Command Prompt window.

Keep this window open during access.

Retrieve Grafana Pod Name:

kubectl get pods --namespace default -l "app.kubernetes.io/name=grafana,app.kubernetes.io/instance=grafana" -o jsonpath="{.items[0].metadata.name}" > grafana_pod_name.txt
set /p GRAFANA_POD_NAME=<grafana_pod_name.txt
del grafana_pod_name.txt
Perform Port Forwarding:


kubectl --namespace default port-forward %GRAFANA_POD_NAME% 3000:3000
Access in Browser:
Navigate to http://localhost:3000 in your web browser. Log in with admin and the password retrieved earlier.

4. Configuring Grafana to Use Prometheus as a Data Source
Once logged into Grafana, you need to connect it to your Prometheus instance.

Navigate to Data Sources:

In Grafana, click the gear icon (Configuration) in the left sidebar.

Select "Data sources".

Click "Add data source" and choose "Prometheus".

Configure Prometheus Data Source:

Name: prometheus (or any name you prefer)

HTTP > URL: This is crucial. Grafana (inside the cluster) needs to reach Prometheus (also inside the cluster) via its Kubernetes Service DNS name.

Since both Prometheus and Grafana were installed in the default namespace, the URL is:

http://prometheus-server.default.svc.cluster.local:80
Note: The Prometheus service is exposing port 80, not 9090, within the cluster.

Access: Browser (default) or Server (default). Server is generally preferred for backend connections.

Scroll down and click "Save & test".
You should see a "Data source is working" message.

## 5. Importing a Kubernetes Cluster Dashboard in Grafana
You can import pre-built Grafana dashboards to visualize your Kubernetes cluster metrics. A common choice is the "Kubernetes Cluster Monitoring (via Prometheus)" dashboard, ID 3662.

Navigate to Dashboards:

In Grafana, click the Dashboards icon (four squares) in the left sidebar.

Select "Import".

Import Dashboard:

In the "Import via grafana.com" field, enter 3662.

Click "Load".

On the next screen, you can choose the folder, and crucially, select your "prometheus" data source from the dropdown menu.

Click "Import".

You will now have a comprehensive dashboard displaying metrics about your Kubernetes nodes, pods, deployments, and the health of core components like the API server and etcd.

## 6. Exposing Kube-State-Metrics (for Direct Access)
Kube-State-Metrics provides rich insights into the state of Kubernetes objects (deployments, pods, nodes, etc.). While Prometheus automatically scrapes these metrics internally, you can expose it via NodePort to access its raw metrics endpoint directly for verification or debugging.

Expose Kube-State-Metrics Service:


kubectl expose service prometheus-kube-state-metrics --type=NodePort --target-port=8080 --name=prometheus-kube-state-metrics-ext
This creates a NodePort service named prometheus-kube-state-metrics-ext.

Verify Service:


kubectl get svc -n default
Look for prometheus-kube-state-metrics-ext and note its assigned NodePort (e.g., 8080:30743/TCP).

Access Kube-State-Metrics via Port Forwarding (for local inspection):

Open a NEW Command Prompt window.

Keep this window open.

Retrieve Kube-State-Metrics Pod Name:


kubectl get pods --namespace default -l "app.kubernetes.io/name=kube-state-metrics,app.kubernetes.io/instance=prometheus" -o jsonpath="{.items[0].metadata.name}" > ksm_pod_name.txt
set /p KSM_POD_NAME=<ksm_pod_name.txt
del ksm_pod_name.txt


Perform Port Forwarding:

kubectl --namespace default port-forward %KSM_POD_NAME% 8080:8080
If port 8080 is in use, you can use an alternative local port, e.g., 8081:8080.

Access in Browser:
Navigate to http://localhost:8080/metrics (or http://localhost:8081/metrics if you used 8081).
You will see a raw text dump of Kubernetes state metrics.