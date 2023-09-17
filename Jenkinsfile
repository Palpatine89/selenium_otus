pipeline {
    agent any
    stages {
        stage('Build image') {
            steps {
                script {
                    docker.build("python-web-tests2", "-f Dockerfile .")
                }
            }
        }
        stage('Run tests') {
            steps {
                script {
                    docker.image('python-web-tests2').run('-v /var/lib/jenkins/workspace:/var/lib/jenkins/workspace python-web-tests2 pytest -n 2 --alluredir=../allure-results -v')
                }
            }
        }
        stage('Reports') {
            steps {
                sh 'ls -la /var/lib/jenkins/workspace/test/allure-results'
                allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: '/var/lib/jenkins/workspace/test/allure-results']]
                ])
            }
        }
    }
}
