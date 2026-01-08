pipeline {
    agent any
    stages {
        stage('Construir') {
            steps {
                // Este comando crea la imagen usando tu Dockerfile
                sh 'docker build -t fase2-jenkins .'
            }
        }
        stage('Comprobar') {
            steps {
                echo '¡La imagen se ha creado bien! Todo correcto.'
            }
        }
    }
}
