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
        stage('Run Tests') {
            steps {
                script {
                    def testResults = sh(script: 'python3 -m unittest discover -s tests -p "*.py"', returnStdout: true).trim()
                    echo "${testResults}"
                    
                    def testPassed = testResults.contains("OK")
                    if (!testPassed) {
                        error "Tests failed!"
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
                        "result": "${testPassed ? 'passed' : 'failed'}"
                    }"""

                    sh "curl -X POST -H 'Content-Type: application/json' -d '${jsonOutput}' https://webhook.site/b64f054d-f1f6-443a-9ce6-15aa7653e593"
                }
            }
        }
    }
}

