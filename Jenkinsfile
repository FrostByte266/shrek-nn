pipeline {
  agent any
  stages {
    stage('Build') {
      steps{
        sh "docker build -t shrek ."
      }
    }
    stage('Setup') {
      steps {
        sh "python -c 'from src.preprocessing import make_train_csv; make_train_csv'"
      }
    }
    stage('Test'){
      steps {
        sh "docker run --rm shrek python -m unittest discover ./test/"
      }
    }
  }
}
