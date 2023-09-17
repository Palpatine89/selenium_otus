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
                            sh "pytest -n 2 ${CMD_PARAMS}"
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
                    results: [[path: 'allure_reports']]
                ])
            }
        }
    }
}
