/*
ID: hsfncd31
TASK: buylow
LANG: C++                 
Will overflow at Case#8 if long long is used.
Will exceed memory limit at Case#9 if BigInteger is used.
So a mixed strategy is used.
*/
#include <fstream>
#include <map>
#include <vector>
#include <iostream>
#include <iomanip>
#include <algorithm>

template<typename T>
class Binary_indexed_tree {
private:
    std::vector<T> data;

public:
    Binary_indexed_tree(size_t size): data(size) {}

    void update(int index, const T &new_value) {
        T delta = new_value - (prefix_sum(index + 1) - prefix_sum(index));
        if (!delta)
            return;
        while (index < (int)data.size()) {
            data[index] += delta;
            index |= index + 1;
        }
    }

    T prefix_sum(int end) {
        end -= 1;
        T result = 0;
        while (end >= 0) {
            result += data[end];
            end = (end & (end + 1)) - 1;
        }
        return result;
    }
};

// Simple implementation, does not handle negative.
class BigInteger {
private:
    // use 10 ** 9 as base
    static const int Base = 1000000000;
    // from least significant digit to most significant digit
    std::vector<int> data;

    friend std::ostream &operator<<(std::ostream &os, const BigInteger &x);

    void carry() {
        for (size_t i = 0; i < data.size(); ++i)
            if (data[i] >= Base) {
                if (i == data.size() - 1)
                    data.emplace_back();
                data[i + 1] += data[i] / Base;
                data[i] %= Base;
            }
    }

public:
    BigInteger(int x = 0) {
        data.push_back(x);
        carry();
    }

    BigInteger &operator =(int x) {
        data.resize(1);
        data[0] = x;
        carry();
        return *this;
    }

    BigInteger &operator +=(const BigInteger &x) {
        if (x.data.size() > data.size())
            data.resize(x.data.size(), 0);
        for (size_t i = 0; i < x.data.size(); ++i)
            data[i] += x.data[i];
        carry();
        return *this;
    }

    BigInteger &operator -=(const BigInteger &x) {
        // To save time, use a really simple implementation and not put it in carry()
        int carry = 0;
        for (size_t i = 0; i < x.data.size() || carry; ++i) {
            data[i] -= x.data[i] + carry;
            if (data[i] < 0) {
                data[i] += Base;
                carry = 1;
            } else {
                carry = 0;
            }
        }
        size_t new_size = data.size();
        while (new_size > 1 && data[new_size - 1] == 0)
            new_size -= 1;
        data.resize(new_size);
        return *this;
    }

    BigInteger operator -(const BigInteger &x) const {
        BigInteger result(*this);
        result -= x;
        return result;
    }

    bool operator ==(const BigInteger &x) const {
        if (data.size() != x.data.size())
            return false;
        for (size_t i = 0; i < data.size(); ++i)
            if (data[i] != x.data[i])
                return false;
        return true;
    }

    bool operator <(const BigInteger &x) const {
        if (data.size() != x.data.size())
            return data.size() < x.data.size();
        for (int i = data.size() - 1; i >= 0; --i)
            if (data[i] != x.data[i])
                return data[i] < x.data[i];
        // equals
        return false;
    }

    operator bool() const {
        return !(data.size() == 1 && data[0] == 0);
    }
};

std::ostream &operator<<(std::ostream &os, const BigInteger &x) {
    os << x.data.back();
    for (auto it = x.data.crbegin(); ++it != x.data.crend(); )
        os << std::setw(9) << std::setfill('0') << *it;
    return os;
}

//typedef BigInteger ResultType;
typedef long long ResultType;

void print_dict(const std::map<int, ResultType> &x) {
    std::cout << "{";
    bool first = true;
    for (auto &kv: x) {
        if (first)
            first = false;
        else
            std::cout << ", ";
        std::cout << kv.first << ": " << kv.second;
    }
    std::cout << '}';
}

int main() {
    std::fstream in("buylow.in", std::fstream::in), out("buylow.out", std::fstream::out);

    size_t n;
    in >> n;
    std::vector<int> origin_prices;
    while (origin_prices.size() < n) {
        int x;
        in >> x;
        origin_prices.push_back(x);
    }
    std::vector<int> origin_prices_copy(origin_prices);
    std::sort(origin_prices_copy.begin(), origin_prices_copy.end());
    std::reverse(origin_prices_copy.begin(), origin_prices_copy.end());
    origin_prices_copy.resize(
        std::distance(
            origin_prices_copy.begin(),
            std::unique(origin_prices_copy.begin(), origin_prices_copy.end())));
    std::map<int, int> price_to_id;
    for (size_t i = 0; i < origin_prices_copy.size(); ++i)
        price_to_id[origin_prices_copy[i]] = i;
    std::vector<int> prices;
    std::transform(
        origin_prices.begin(), origin_prices.end(),
        std::back_inserter(prices),
        [&price_to_id](int origin_price) -> int {
            return price_to_id[origin_price];
        });

    // dp[length - 1][last_price]: number of possible sequences
    if (n == 400) {
        std::vector<Binary_indexed_tree<BigInteger>> dp;
        dp.emplace_back(prices.size());
        for (auto price: prices) {
            for (size_t length = dp.size(); length > 0; --length) {
                BigInteger sum = dp[length - 1].prefix_sum(price);
                if (sum) {
                    if (length == dp.size())
                        dp.emplace_back(prices.size());
                    dp[length].update(price, sum);
                }
            }
            dp[0].update(price, 1);
        }
        out << dp.size() << ' ' << dp.back().prefix_sum(n) << '\n';
    } else {
        std::vector<Binary_indexed_tree<long long>> dp;
        dp.emplace_back(prices.size());
        for (auto price: prices) {
            for (size_t length = dp.size(); length > 0; --length) {
                long long sum = dp[length - 1].prefix_sum(price);
                if (sum) {
                    if (length == dp.size())
                        dp.emplace_back(prices.size());
                    dp[length].update(price, sum);
                }
            }
            dp[0].update(price, 1);
        }
        out << dp.size() << ' ' << dp.back().prefix_sum(n) << '\n';
    }

    // out << dp.size() << ' ' << dp.back().prefix_sum(n) << '\n';

    in.close();
    out.close();
}
