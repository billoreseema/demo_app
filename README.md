
# Chaos Engineering Demo 

This project is created as part of university research for the topic - Analysis of Micro service Resilience with novel fault injection on multi-cloud environment 




## Acknowledgements

 - [Instana Sample robot-shop app](https://github.com/instana/robot-shop)
 - [Chaos Mesh Project](https://github.com/chaos-mesh/chaos-mesh)



## Installation

Install application using helm

```bash
  kubectl create ns robot-shop
  cd K8s/helm
  helm repo add cloud-native-toolkit https://charts.cloudnativetoolkit.dev

```
  Create persistence volumn for the redis manually
```bash
  kubectl apply -f pv-volume.yaml
  kubectl apply -f pv-claim.yaml
```
  Install robot-shop app
```bash
  helm install robot-shop --namespace robot-shop .
  helm upgrade robot-shop --namespace robot-shop .
  kubectl get pods -n robot-shop
```
  Install Chaos-mesh on Azure
```bash
  kubectl create ns chaos-testing
  helm install chaos-mesh chaos-mesh/chaos-mesh -n=chaos-testing --version 2.3.0 --set dashboard.securityMode=false  --set chaosDaemon.runtime=containerd 
--set chaosDaemon.socketPath= /run/containerd/containerd.sock 
--set hostNetwork=true
  kubectl get pods -n chaos-testing
```
  Inject Faults
```bash
  kubectl apply -f netrob2.yml -n robot-shop 
  kubectl describe networkchaos <chaos-name>
  kubectl annotate networkchaos network-delay experiment.chaos-mesh.org/pause=true
  kubectl delete networkchaos network-delay
```
  Run Load Test using Locust 
```bash
  locust -f robot-shop.py --host http://<hostname/IP>:8080 --headless -r 1 -u 100 --csv=demo -t30m
```
  Run Load Test using Jmeter 
```bash
  robotshop.jmx
```
  To Generate DAG
```bash
  map.py
```
