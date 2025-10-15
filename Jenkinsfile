pipeline {
    agent any

    stages {
        stage('Debug Environment') {
            steps {
                echo 'Checking Python and Docker versions...'
                bat 'python --version'
                bat 'docker --version'
            }
        }

        stage('Clone Repository') {
            steps {
                echo 'Cloning the repo...'
                checkout scm
            }
        }

        stage('Build Python Environment') {
            steps {
                echo 'Installing Python dependencies...'
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install flask pytest'
            }
        }

        stage('Test') {
            steps {
                echo 'Running pytest...'
                bat 'python -m pytest test_app.py'
            }
        }

        stage('Docker Build & Test') {
            steps {
                echo 'Building Docker image...'
                bat 'docker build -t student-app:latest .'
                echo 'Testing container...'
                bat 'docker run --rm student-app:latest python -m pytest test_app.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying container...'
                bat 'docker rm -f student-app-deploy || echo "No existing container"'
                bat 'docker run -d -p 5000:5000 --name student-app-deploy student-app:latest'
                echo 'Deployment successful! Visit http://localhost:5000'
            }
        }
    }

    post {
        success {
            echo '🎉 Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
    }
}
