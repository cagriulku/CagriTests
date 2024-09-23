
pipeline {
    agent any
    parameters {
        string(name: 'node_count', defaultValue: '1', description: 'Number of nodes (min=1, max=5)')
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
       stage('Check Selenium Grid Health') {
          steps {
             script {
                 def gridHealth = sh(script: 'python3 SeleniumGridHealthCheck.py', returnStdout: true).trim()
                 echo "${gridHealth}"

                   if (!gridHealth.contains("Selenium Grid is ready!")) {
                        error "Grid health check failed!"
                       }
                     }
                  }
               }
        stage('Run Tests') {
            steps {
                script {
                    def testResultsString = sh(script: 'python3 -m unittest tests/test_string_operations.py', returnStdout: true).trim()
                    echo "${testResultsString}"

                    def testResultsMath = sh(script: 'python3 -m unittest tests/test_math_operations.py', returnStdout: true).trim()
                    echo "${testResultsMath}"

                    if (testResultsString.contains("OK") && testResultsMath.contains("OK")) {
                        echo "all tests passed!"
                    } else {
                        error "all Tests failed!"
                    }
                }
            }
        }
        stage('Send Results') {
            steps {
                script {
                    def buildNumber = currentBuild.number
                    def nodes = params.node_count
                    currentBuild.displayName = "Build_Name_${buildNumber}_Nodes_${nodes}"

                    def jsonOutput = """{
                        "build_name": "Cagri_Build_Name_${buildNumber}",
                        "node_count": ${nodes},
                        "test_ result": "passed"
                    }"""

                    sh "curl -X POST -H 'Content-Type: application/json' -d '${jsonOutput}' https://webhook.site/b64f054d-f1f6-443a-9ce6-15aa7653e593"
                }
            }
        }
    }
}
