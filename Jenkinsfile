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

    }
}