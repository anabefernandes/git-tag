pipeline {
    agent any

    environment {
        GIT_TAG = sh(script: 'git describe --tags --exact-match || echo "no_tag"', returnStdout: true).trim()
    }

    stages {
        stage('Verificar Tag') {
            steps {
                script {
                    if (env.GIT_TAG != "no_tag") {
                        echo "Este commit foi disparado por uma tag: ${env.GIT_TAG}"
                    } else {
                        echo "Este commit não é uma tag. Nenhuma ação especial será executada."
                    }
                }
            }
        }
        
        stage('Build Release') {
            when {
                expression { env.GIT_TAG != "no_tag" }
            }
            steps {
                echo "Executando build de release para versão ${env.GIT_TAG}"
                // Adicione aqui comandos específicos para build de release
            }
        }
    }

    post {
        always {
            echo "Build finalizado."
        }
    }
}