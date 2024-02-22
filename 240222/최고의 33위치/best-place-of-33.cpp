#include <iostream>
#include <algorithm>

#define MAX_N 20

using namespace std;

int n;
int grid[MAX_N][MAX_N];

int GetNumOfGold(int row_s, int col_s, int row_e, int col_e) {
    int num_of_gold = 0;

    for(int i = row_s; i <= row_e; i++) {
        for(int j = col_s; j <= col_e; j++) {
            num_of_gold += grid[i][j];
        }
    }
    return num_of_gold;
}

int main() {
    int max_gold = 0;

    int n;
    cin >> n;
    for(int row = 0; row < n; row++)
        for(int col = 0; col < n; col++)
            cin >> grid[row][col];

    for(int row = 0; row < n; row++) {
        for(int col = 0; col < n; col++) {
            if(row + 2 >= n || col + 2 >= n) continue;

            int num_of_gold = GetNumOfGold(row, col, row+2, col+2);

            max_gold = max(max_gold, num_of_gold);
        }
    }
    
    cout << max_gold;
    
    return 0;
}