pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps { git 'https://github.com/openshift09/ci-basic-python' }
    }
    stage('Build') {
      steps { sh 'python3 app.py' }
    }
  }
}

