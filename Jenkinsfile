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
        sh "docker run --rm -d -t --name nn_container shrek bash"
        sh "docker exec nn_container python -c 'from src.preprocessing import make_train_csv; make_train_csv()'"
      }
    }
    stage('Test'){
      steps {
        sh "docker exec nn_container python -m unittest discover ./test/"
      }
    }
    stage('Cleanup') {
      steps {
        sh "docker kill nn_container"
      }
    }
  }
}
