/*
ID: hsfncd31
TASK: nocows
LANG: C++                 
*/
#include <fstream>

static const int MAXN = 200 - 1, MAXK = 100 - 1, MOD = 9901;
int dp[MAXN + 1][MAXK + 1];

int main() {
    std::fstream in("nocows.in", std::fstream::in), out("nocows.out", std::fstream::out);

    int N, K;

    in >> N >> K;
    dp[0][0] = dp[1][1] = 1;
    for (int n = 2; n <= N; ++n)
        for (int k = 0; k <= std::min(n, K); ++k)
            for (int left_n = 1; left_n < n - 1; ++left_n) {
                for (int smaller_k = 1; smaller_k < k - 1; ++smaller_k) {
                    dp[n][k] += dp[left_n][k - 1] * dp[n - 1 - left_n][smaller_k];
                    dp[n][k] += dp[left_n][smaller_k] * dp[n - 1 - left_n][k - 1];
                    dp[n][k] %= MOD;
                }
                dp[n][k] += dp[left_n][k - 1] * dp[n - 1 - left_n][k - 1];
                dp[n][k] %= MOD;
            }
    out << dp[N][K] << '\n';

    in.close();
    out.close();
}
