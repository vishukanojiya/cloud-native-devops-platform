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

GitHub → Jenkins → Docker → Trivy → Registry → Argo CD → Kubernetes

## Current Status

- FastAPI backend
- PostgreSQL
- Docker
- Docker Compose
- Database migrations
- Seed data
- GitHub repository

## Local Development

```bash
docker compose -f docker/docker-compose.yml up -d