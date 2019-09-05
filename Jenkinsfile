pipeline {
  agent {dockerfile true}
  stages {
    stage('Test') {
      steps{
        sh "pythom -m unittest discover ./test/"
      }
    }
  }
}
