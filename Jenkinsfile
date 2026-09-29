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
        stage('Docker Push') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USERNAME',
                    passwordVariable: 'DOCKER_PASSWORD'
                )]) {
                    sh '''
                        echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
                        docker tag cloud-native-backend:${BUILD_NUMBER} vishalkaojiya/cloud-native-backend:${BUILD_NUMBER}
                        docker push vishalkaojiya/cloud-native-backend:${BUILD_NUMBER}
                    '''
                }
            }
        }

    }
}