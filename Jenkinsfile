pipeline {
  agent any

  options {
    buildDiscarder(logRotator(numToKeepStr:'5'))
    timestamps()
  }

  environment {
    PATH = "$PATH:~/.local/bin"
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
    changed {
      mail subject: "Build status of ${JOB_NAME} changed to ${currentBuild.result}", to: 'paul.trampert@ptrampert.com', body: "Build log attached."
    }
  }
}