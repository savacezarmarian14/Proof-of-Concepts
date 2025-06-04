// vuln-server.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <netinet/in.h>

#define PORT 9002
#define BUF_SIZE 1024

int main() {
    int server_fd, client_fd;
    struct sockaddr_in addr;
    char buffer[BUF_SIZE];

    server_fd = socket(AF_INET, SOCK_STREAM, 0);

    addr.sin_family = AF_INET;
    addr.sin_port = htons(PORT);
    addr.sin_addr.s_addr = INADDR_ANY;

    bind(server_fd, (struct sockaddr*)&addr, sizeof(addr));
    listen(server_fd, 1);

    printf("Server listening on port %d...\n", PORT);

    while (1) {
        client_fd = accept(server_fd, NULL, NULL);
        memset(buffer, 0, BUF_SIZE);

        ssize_t len = recv(client_fd, buffer, BUF_SIZE, 0);
        if (len > 0) {
            printf("Received: %s\n", buffer);

            if (strncmp(buffer, "BOOM", 4) == 0) {
                printf("Crash triggered!\n");
                *(int*)0 = 0;  // Forced crash
            }
        }

        close(client_fd);
    }

    close(server_fd);
    return 0;
}
