pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout code from SCM
git 'https://github.com/sudheeraddala/project1111.git'
            }
        }
        stage('Build') {
            steps {
                // Execute build commands
                sh 'mvn clean package'
            }
        }
        stage('Test') {
            steps {
                // Execute test commands
                sh 'mvn test'
            }
        }
        stage('Deploy') {
            steps {
                // Execute deployment commands
                sh 'kubectl apply -f deployment.yaml'
            }
        }
    }
    
    post {
        success {
            // Actions to take if the pipeline succeeds
            echo 'Pipeline succeeded!'
        }
        failure {
            // Actions to take if the pipeline fails
            echo 'Pipeline failed!'
        }
    }
}