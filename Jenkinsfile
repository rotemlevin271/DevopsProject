pipeline {
    agent any
    
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
        
        stage('Run Backend') {
            steps {
                script {
                    try {
                        bat 'python my_project/test.py'
                    }
                    catch (err) {
                        println err
                    }
                }
                // Run rest_app.py (backend)
                bat 'start /min python my_project/rest_app.py'
            }
        }
        
        stage('Run Frontend') {
            steps {
                // Run web_app.py (frontend)
                bat 'start /min python my_project/web_app.py'
            }
        }
        
        stage('Run Backend Testing') {
            steps {
                // Run backend_testing.py
                script {
                    try {
                        bat 'python my_project/backend_testing.py'
                    }
                    catch (err){
                        println err
                    }
                }
            }
        }
        
        stage('Run Frontend Testing') {
            steps {
                // Run frontend_testing.py
                bat 'python my_project/frontend_testing.py'
            }
        }
        
        stage('Run Combined Testing') {
            steps {
                // Run combined_testing.py
                bat 'python my_project/combined_testing.py'
            }
        }
        
        stage('Run Clean Environment') {
            steps {
                // Run clean_environment.py
                bat 'python my_project/clean_environment.py'
            }
        }
    }
}
