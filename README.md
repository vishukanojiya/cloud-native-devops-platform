# Cloud-Native DevOps & SRE Platform

A production-style DevOps project demonstrating:

- AWS
- Terraform
- Ansible
- Docker
- Kubernetes
- Nginx
- Jenkins
- Argo CD
- Prometheus
- Grafana
- Loki
- Alertmanager
- Trivy
- Helm
- GitHub
- PostgreSQL

## Architecture

GitHub → Jenkins → Docker → Registry → Argo CD → Kubernetes

Observability:

Prometheus → Grafana
Loki → Grafana
Alertmanager → Notifications

Infrastructure:

Terraform → AWS
Ansible → Configuration Management
