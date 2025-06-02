#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define SERVER_PORT 9001
#define SERVER_ADDR "127.0.0.1"
#define BUF_SIZE 1024

int main() {
    int sockfd;
    struct sockaddr_in serv_addr;
    char buffer[BUF_SIZE];

    // Creează socket
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        perror("socket");
        return 1;
    }

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(SERVER_PORT);
    inet_pton(AF_INET, SERVER_ADDR, &serv_addr.sin_addr);

    // Conectează la server
    if (connect(sockfd, (struct sockaddr*)&serv_addr, sizeof(serv_addr)) < 0) {
        perror("connect");
        close(sockfd);
        return 1;
    }

    // Trimite din stdin în buclă
    ssize_t read_len;
    while ((read_len = read(STDIN_FILENO, buffer, BUF_SIZE)) > 0) {
        send(sockfd, buffer, read_len, 0);
    }

    // Închide socketul
    close(sockfd);
    return 0;
}
