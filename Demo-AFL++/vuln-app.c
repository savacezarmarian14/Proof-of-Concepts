#include <stdio.h>
#include <string.h>

int main(int argc, char** argv) {
    char buf[8];
    fgets(buf, 64, stdin);  // vulnerability here: buffer overflow
    if (buf[0] == 'A' && buf[1] == 'B' && buf[2] == 'C')
        *(int*)0 = 0;  // forced crash
    return 0;
}
