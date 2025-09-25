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
                sh 'python3 test_hello.py'
            }
        }
        
        stage('Build') {
            steps {
                sh 'python3 hello.py'
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'echo "Application would be deployed here"'
                sh 'echo "Deployment to cloud platform would happen here"'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline completed'
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
