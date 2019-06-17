pipeline {
  agent any

  options {
    buildDiscarder(logRotator(numToKeepStr:'5'))
    timestamps()
  }

  stages {
    stage('Test') {
      steps {
        sh 'molecule test --all --destroy=always'
      }
    }
  }

  post {
    always {
      deleteDir()
    }
    regression {
      mail subject: 'Build status of ${JOB_NAME} changed to ${currentBuild.result}', to: 'paul.trampert@ptrampert.com'
    }
  }
}