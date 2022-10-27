class Solution {
public:
    int largestOverlap(vector<vector<int>>& img1, vector<vector<int>>& img2) {
        int n = img1.size();
        if(n<2) return img1[0][0] & img2[0][0];
        int ans = 0;
        for(int i=-n+1; i<n; i++) {
            for(int j=-n+1; j<n; j++) {
                int cnt = 0;
                for(int k=0; k<n; k++) {
                    for(int l=0; l<n; l++) {
                        if(i+k>-1 && i+k<n && j+l>-1 && j+l<n) {
                            if(img1[i+k][j+l] & img2[k][l]) cnt++;
                        }
                    }
                }
                ans = cnt > ans ? cnt : ans;    
            }
        }
        return ans;
    };
};
