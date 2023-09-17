pipeline {
    agent any
    stages {
        stage("Build image") {
            steps {
                catchError {
                    script {
                        docker.build("python-web-tests2", "-f Dockerfile .")
                    }
                }
            }
        }
        stage('Run tests') {
            steps {
                catchError {
                    script {
                        docker.image('python-web-tests2').inside() {
                            // Создаем каталог allure-results и устанавливаем правильные разрешения
                            sh "mkdir -p allure-results"
                            sh "chmod 777 allure-results"
                            sh "pytest -n 2"
                        }
                    }
                }
            }
        }
        stage('Reports') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }
}
