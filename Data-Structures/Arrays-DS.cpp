#include <iostream>
#include <vector>
using namespace std;

vector<int> reverseArray(vector<int>& A) {
    int n = A.size();
    vector<int> reversedArray(n);

    for (int i = 0; i < n; ++i) {
        reversedArray[i] = A[n - 1 - i];
    }

    return reversedArray;
}

int main() {
    int n;
    cin >> n;  
    vector<int> A(n);

    for (int i = 0; i < n; ++i) {
        cin >> A[i];
    }

    vector<int> result = reverseArray(A);

    for (int i = 0; i < result.size(); ++i) {
        cout << result[i] << " ";
    }
    cout << endl;

    return 0;
}
