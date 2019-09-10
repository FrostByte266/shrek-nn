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
        sh "docker run --rm --name shrek_container shrek"
        sh "docker exec shrek_container python -c 'from src.preprocessing import make_train_csv; make_train_csv'"
      }
    }
    stage('Test'){
      steps {
        sh "docker exec shrek_container python -m unittest discover ./test/"
      }
    }
  }
}
