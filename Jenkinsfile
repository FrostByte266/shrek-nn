pipeline {
  agent {dockerfile true}
  stages {
    stage('Test') {
      sh "pythom -m unittest discover ./test/"
    }
  }
}
