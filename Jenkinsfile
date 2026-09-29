pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                echo 'Running application tests...'
            }
        }
        stage('Docker Build') {
            steps {
                sh 'docker build -t cloud-native-backend:${BUILD_NUMBER} ./application/backend'
            }
        }
        stage('Trivy Scan') {
            steps {
                sh '''
                    docker run --rm \
                    -v /var/run/docker.sock:/var/run/docker.sock \
                    aquasec/trivy:latest \
                    image --severity HIGH,CRITICAL --exit-code 1 cloud-native-backend:${BUILD_NUMBER}
                '''
            }
        }

    }
}