int reverse(int x){
    int ans = 0;
    int digit = 0;
    char s[12];
    sprintf(s, "%d", x);
    for(int i=strlen(s)-1; i>-1; i--) {
        if(s[i]=='-') {
            ans *= -1;
        } else {
            
            digit = s[i]-48;
            if(ans>214748364) return 0;
            ans *= 10;
            if(ans>2147483647-digit) return 0;
            ans += digit;
            printf("%d\n", ans);
        }
    }
