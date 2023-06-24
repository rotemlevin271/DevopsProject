pipeline {
    agent any
    
    environment {
    DOCKERHUB_CREDENTIALS = credentials('docker_hub')
    }
    
    options {
        buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '5'))
    }
    
    stages {
        stage('Pull Code') {
            steps {
                script {
                    try {
                        bat 'rmdir /s /q my_project'
                    }
                    catch (err) {
                        bat 'ls'
                    }
                }
                // Pull code from your GitHub repository holding your previous project (part 1)
                bat 'git.exe clone https://github.com/rotemlevin271/DevopsProject.git my_project'
            }
        }
        
        stage('Install requirements') {
            steps {
                bat 'python -m pip install -r my_project/requirements.txt'
            }
        }
        
        // stage('Run Backend') {
        //     steps {
        //         script {
        //             try {
        //                 bat 'python my_project/test.py'
        //             }
        //             catch (err) {
        //                 println err
        //             }
        //         }
        //         // Run rest_app.py (backend)
        //         bat 'start /min python my_project/rest_app.py'
        //     }
        // }
        
        
        // stage('Run Backend Testing') {
        //     steps {
        //         // Run backend_testing.py
        //         script {
        //             try {
        //                 bat 'python my_project/backend_testing.py'
        //             }
        //             catch (err){
        //                 println err
        //             }
        //         }
        //     }
        // }
        
        
        // stage('Run Clean Environment') {
        //     steps {
        //         // Run clean_environment.py
        //         bat 'python my_project/clean_environment.py'
        //     }
        // }
        
        stage('Build Docker Image') {
            steps {
                // Build Docker Image for rest_app
                bat 'docker build -t rest_app my_project/.'
            }
        }
        
        stage('Login to Docker HUB') {
            steps {
                // login to docker HUB
                withCredentials([usernamePassword(credentialsId: 'docker_hub', passwordVaroable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                    bat "echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin"            
                }
            }
        }
        
        stage('Push Docker Image') {
            steps {
                // Push Docker Image to hub
                bat 'docker push rest_app'
            }
        }
        
        stage('Set Compose Image Version') {
            steps {
                // setting the image version for compose
                bat "echo 'COMPOSE_VERSION=3.8' > .env"
            }
        }
        
        stage('Run Docker Compose-up') {
            steps {
                // Run docker compose 
                bat 'docker-compose -f my_project/docker-compose.yml up -d'
            }
        }
        
        stage('Run Docker Backend Testing') {
            steps {
                // Run docker_backend_testing.py
                script {
                    try {
                        bat 'python my_project/docker_backend_testing.py'
                    }
                    catch (err){
                        println err
                    }
                }
            }
        }
        
        stage('Clean Environment') {
            steps {
                // compose-down&delete local image 
                bat 'docker-compose down'
                bat 'docker rmi rest_app'
            }
        }
    }
}
