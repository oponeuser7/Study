#include <algorithm>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        string sum1 = "";
        string sum2 = "";
        for(string s: word1) {
            sum1 += s;
        }
        for(string s: word2) {
            sum2 += s;
        }
        return sum1 == sum2;
    }
};