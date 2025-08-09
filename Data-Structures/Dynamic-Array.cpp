#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> dynamicArray(int n, vector<string>& queries) {
    vector<vector<int>> arr(n);
    vector<int> results;         
    int last_answer = 0;

    for (const string& query : queries) {
        int type, x, y;
        sscanf(query.c_str(), "%d %d %d", &type, &x, &y);  

        int idx = (x ^ last_answer) % n;

        if (type == 1) {
        
            arr[idx].push_back(y);
        } else if (type == 2) {
         
            int size = arr[idx].size();
            last_answer = arr[idx][y % size];
            results.push_back(last_answer);
        }
    }

    return results;
}

int main() {
    int n, q;
    cin >> n >> q;
    cin.ignore();  
    vector<string> queries(q);
    for (int i = 0; i < q; ++i) {
        getline(cin, queries[i]);  
    }

    vector<int> results = dynamicArray(n, queries);

    for (int result : results) {
        cout << result << endl;
    }

    return 0;
}
