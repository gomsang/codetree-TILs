#include <iostream>

using namespace std;

#define LIST_MAX 100

int stack[LIST_MAX];


int delBlock(int n, int s, int e) {
    int startpos = n - e;
    int endpos = n - s;
    for(int i = startpos; i < (n - (e - s + 1)); i++) {
        stack[i] = stack[endpos + (i - startpos) + 1];
    }
    return e - s + 1;
}


int main() {
    int n;
    cin >> n;

    for(int i = 0; i < n; i++){
        cin >> stack[n - i - 1];
    }

    int s, e;
    cin >> s >> e;
    n -= delBlock(n, s, e);
    cin >> s >> e;
    n -= delBlock(n, s, e);

    cout << n << endl;
     for(int i = n - 1; i >= 0; i--){
        cout << stack[i] << endl;
    }
    return 0;
}