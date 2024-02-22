#include <iostream>
#define MAX_N 200

using namespace std;

int belt[MAX_N * 2];

int main() {
    int n, t;
    cin >> n >> t;

    for(int i = 0; i < n * 2; i++) {
        cin >> belt[i];
    }

    for(int i = 0; i < t; i++) {
        int last = belt[n * 2 - 1];
        for(int i = n * 2 - 1; i > 0; i--) {
            belt[i] = belt[i - 1];
        }
        belt[0] = last;
    }

   for(int i = 0; i < n * 2; i++) {
        cout << belt[i] << " ";
        if(i == n - 1) {
            cout << endl;
        }
    }
    

    return 0;
}