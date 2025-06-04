#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main() {
    int sockfd, clientfd;
    struct sockaddr_in addr;
    char buffer[64] = {0};

    sockfd = socket(AF_INET, SOCK_STREAM, 0);

    addr.sin_family = AF_INET;
    addr.sin_port = htons(9001);
    addr.sin_addr.s_addr = INADDR_ANY;

    bind(sockfd, (struct sockaddr*)&addr, sizeof(addr));
    listen(sockfd, 1);

    printf("Server waiting for connection on port 9001...\n");

    clientfd = accept(sockfd, NULL, NULL);
    printf("Client connected.\n");
    while (1) {
        int n = recv(clientfd, buffer, sizeof(buffer), 0);
        if (n > 0) {
            printf("Received: %.*s\n", n, buffer);

            if (buffer[0] == 'F' && buffer[1] == 'U' && buffer[2] == 'Z') {
                printf("Crash triggered!\n");
                *(int*)0 = 0;  // Intentional crash
            }
        }
    } 

    close(clientfd);
    close(sockfd);
    return 0;
}
