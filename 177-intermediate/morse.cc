#include <iostream>
#include <string>
using namespace std;

int main() {

    string morse[] {
        ".-", // A  
        "-...", // B
        "-.-.", // C
        "-.." , // D
        ".", // E
        "..-.", // F
        "--.", // G
        "....", // H
        "..", // I
        ".---", // J
        "-.-", // K
        ".-..", // L
        "--", // M
        "-.", // N
        "---", // O
        ".--.", // P
        "--.-", // Q
        ".-.", // R
        "...", // S
        "-", // T
        "..--", // U
        "...-", // V
        ".--", // W
        "-..-", // X
        "-.--", // Y
        "--.." // Z
    };

    int ascii[] {
        97,98,99,100,101,102,103,104,105,106,107,108,109,110,
        111,112,113,114,115,116,117,118,119,120,121,122
    };

    string input;
    string message;
    cin >> input;

    for (int i = 0; i < input.length(); i++) {
        input[i] = tolower(input[i]);
        for (int j = 0; j < 26; j++) {
            if (input[i] == ascii[j]) {
                message += morse[j];
            }
        }
    }

    cout << message << endl;

    return 0;
}
