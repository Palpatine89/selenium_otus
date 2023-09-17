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
        stage("Run tests") {
            steps {
                catchError {
                    script {
                        // Запускаем Docker-контейнер с созданным образом
                        def myImage = docker.image('python-web-tests2')
                        myImage.inside("--entrypoint=''") {
                            sh "pytest -n 2 --alluredir=../allure-results -v"
                        }
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
