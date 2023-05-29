pipeline {
    agent any

    stages {
        
        stage('build docker container') {
            steps {
                sh 'docker build . --tag ttl.sh/yordan-flask-app:1h'
            }
        }

        stage('push docker container') {
            steps {
                sh 'docker push ttl.sh/yordan-flask-app:1h'
            }
        }

        stage('pull docker container') {
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'target-ssh-credentials', keyFileVariable: 'keyFile', usernameVariable: 'userName')]) {
                    sh "ssh-keyscan 192.168.105.3 > ~/.ssh/known_hosts"
                    sh "ssh -l ${userName} -i ${keyFile} 192.168.105.3 -C docker pull ttl.sh/yordan-flask-app:1h"
                }
            }
        }

        stage('run docker container'){
            steps{
                withCredentials([sshUserPrivateKey(credentialsId: 'target-ssh-credentials', keyFileVariable: 'keyFile', usernameVariable: 'userName')]) {
                    sh "ssh-keyscan 192.168.105.3 > ~/.ssh/known_hosts"
                    sh "ssh -l ${userName} -i ${keyFile} 192.168.105.3 -C docker rm --force yordan-flask-app"
                    sh "ssh -l ${userName} -i ${keyFile} 192.168.105.3 -C docker run --detach --publish 5000:5000 --name yordan-flask-app ttl.sh/yordan-flask-app:1h"
                }
            }
        }

        stage('health check'){
            steps{
                sh "curl -s http://192.168.105.3:5000/api"
            }
        }
    }
}