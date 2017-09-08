Jenkinsfile (Declarative Pipeline)
pipeline {
    agent { docker 'python:3.6.2' }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}