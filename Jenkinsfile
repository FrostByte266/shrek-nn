pipeline {
  agent any
  stages {
    stage('Build') {
      steps{
        sh "docker build -t shrek ."
      }
    }
    stage('Test'){
      steps {
        sh "docker run --rm shrek python -m unittest discover ./test/"
      }
    }
  }
}
