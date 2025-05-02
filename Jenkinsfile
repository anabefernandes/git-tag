pipeline {
    agent any

    environment {
        GIT_TAG = sh(script: 'git describe --tags --exact-match || echo "no_tag"', returnStdout: true).trim()
    }

    stages {
        stage('Verificar Tag') {
            steps {
                script {
                    //se o commit for uma tag, executa o build de release
                    if (env.GIT_TAG != "no_tag") {
                        echo "Este commit foi disparado por uma tag: ${env.GIT_TAG}"
                        echo "Executando build de release para a versão ${env.GIT_TAG}"
                    } else {
                        echo "Este commit não é uma tag. Nenhuma ação especial será executada."
                    }
                }
            }
        }
    }

    post {
        always {
            echo "Build finalizado."
        }
    }
}
