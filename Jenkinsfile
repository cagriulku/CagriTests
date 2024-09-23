pipeline {
    agent any
    parameters {
        string(name: 'node_count', defaultValue: '1', description: 'Number of nodes (min=1, max=5)')
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Check Selenium Grid Health') {
            steps {
                script {
                    sh 'python3 SeleniumGridHealthCheck.py'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    sh 'python3 -m unittest discover -s tests'
                }
            }
        }
        stage('Send Results') {
            steps {
                sh 'curl -X POST -H "Content-Type: application/json" -d "{\\"result\\": \\"Test passed\\"}" https://webhook.site/b64f054d-f1f6-443a-9ce6-15aa7653e593'
            }
        }
    }
}


