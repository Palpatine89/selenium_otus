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
        stage('Reports') {
            steps {
                catchError {
                    script {
                        // Убедитесь, что путь к allure-results правильно настроен
                        sh "ls -la allure-results"
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
    }
}
