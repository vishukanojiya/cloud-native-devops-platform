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
                    image --severity HIGH,CRITICAL --ignore-unfixed --exit-code 1 cloud-native-backend:${BUILD_NUMBER}
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
        stage('Update GitOps Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'github-push',
                    usernameVariable: 'GIT_USERNAME',
                    passwordVariable: 'GIT_PASSWORD'
                )]) {
                    sh '''
                        sed -i "s/newTag: \".*\"/newTag: \"${BUILD_NUMBER}\"/" kubernetes/overlays/dev/kustomization.yaml

                        git config user.name "Jenkins"
                        git config user.email "jenkins@local"

                        git add kubernetes/overlays/dev/kustomization.yaml
                        git commit -m "Update backend image to ${BUILD_NUMBER}"

                        git push https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/vishukanojiya/cloud-native-devops-platform.git HEAD:main
                    '''
                }
            }
        }
    }
}