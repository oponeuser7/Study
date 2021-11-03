int sum(int x,int y) {
    return x + y;
}
int fibonacci(int n) {
    if(n < 2) {
        return n;
    }
    return fibonacci(n-1) + fibonacci(n-2);
}
int main() {
    int x = 1;
    int y = 2;
    int z;
    z = sum(x, y);
}