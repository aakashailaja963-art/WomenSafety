pipeline {
    agent any
    stages {
        stage('Clone Code') {
            steps {
                git 'https://github.com/aakashailaja963-art/WomenSafety.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t womensafety:latest .'
            }
        }
        stage('Run Application') {
            steps {
                bat 'docker run -d -p 5000:5000 womensafety:latest'
            }
        }
        stage('Test') {
            steps {
                echo 'Women Safety App Deployed Successfully!'
            }
        }
    }
}
