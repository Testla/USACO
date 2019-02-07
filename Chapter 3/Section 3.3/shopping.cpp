/*
ID: hsfncd31
TASK: shopping
LANG: C++                 
*/
#include <fstream>
#include <map>
#include <vector>
#include <array>
#include <algorithm>
#include <iostream>

class NDArray {
public:
    std::vector<int> data;
    std::vector<int> element_size;

    NDArray(const std::vector<int> &size) {
        int s = 1;
        element_size.resize(size.size());
        for (int i = size.size() - 1; i >= 0; --i) {
            element_size[i] = s;
            s *= size[i];
        }
        data.resize(s);
    }

    inline int &operator [](int key) {
        return data[key];
    }

    inline int &operator [](const std::vector<int> &key) {
        return this->operator[](location_of(key));
    }

    int location_of(const std::vector<int> &key) {
        int result = 0;
        for (size_t i = 0; i < element_size.size(); ++i)
            result += key[i] * element_size[i];
        return result;
    }
};

// range: [(lower_bound, upper_bound)], upper_bound not included
// Returns whether the end is reached.
bool next_cartesian_product(
        std::vector<int> &x, const std::vector<std::pair<int, int>> &ranges,
        int &value, const std::vector<int> &weight) {
    int carry = 1;
    for (int i = x.size() - 1; i >= 0 && carry; --i) {
        x[i] += carry;
        value += weight[i];
        if (x[i] == ranges[i].second) {
            x[i] = ranges[i].first;
            value -= (ranges[i].second - ranges[i].first) * weight[i];
            carry = 1;
        } else {
            carry = 0;
        }
    }
    return bool(carry == 0);
}

int main() {
    std::fstream in("shopping.in", std::fstream::in), out("shopping.out", std::fstream::out);

    int s;
    in >> s;
    // [({code: number}, price)]
    std::vector<std::pair<std::map<int, int>, int>> special_offers;
    for (int _ = 0; _ < s; ++_) {
        special_offers.emplace_back();
        int n, c, k;
        in >> n;
        for (int _ = 0; _ < n; ++_) {
            in >> c >> k;
            special_offers.back().first[c] = k;
        }
        in >> special_offers.back().second;
    }
    int b;
    std::vector<std::array<int, 3>> products_to_buy;
    std::vector<int> product_codes, product_counts, product_prices;
    in >> b;
    if (b == 0) {
        // Case#3 is "0\n0\n"...
        out << "0\n";
        return 0;
    }
    for (int _ = 0; _ < b; ++_) {
        int c, k, p;
        in >> c >> k >> p;
        products_to_buy.push_back({c, k, p});
        product_codes.push_back(c);
        product_counts.push_back(k);
        product_prices.push_back(p);
    }

    std::vector<int> count_plus_1;
    std::transform(product_counts.begin(), product_counts.end(), std::back_inserter(count_plus_1), [](int x) -> int { return x + 1; });
    NDArray best(count_plus_1);
    std::vector<std::pair<int, int>> ranges;
    std::transform(product_counts.begin(), product_counts.end(), std::back_inserter(ranges), [](int x) -> std::pair<int, int> { return std::make_pair(0, x + 1); });
    std::vector<int> temp_counts(product_counts.size());

    // initialize best
    // actually both total_price and index can be calculated incrementally
    int total_price = 0;
    for (int i = 0; ; ++i) {
        best[i] = total_price;
        if (!next_cartesian_product(temp_counts, ranges, total_price, product_prices))
            break;
    }

    for (auto &special_offer: special_offers) {
        bool ok = true;
        std::vector<int> offer_product_counts(product_counts.size());
        for (auto &kv: special_offer.first) {
            auto code_position = std::find(product_codes.begin(), product_codes.end(), kv.first);
            if (code_position == product_codes.end()) {
                // contains unwanted product
                ok = false;
                break;
            }
            offer_product_counts[code_position - product_codes.begin()] = kv.second;
        }
        if (!ok)
            continue;

        // update ranges
        for (size_t i = 0; i < offer_product_counts.size(); ++i)
            ranges[i].second = std::max(product_counts[i] - offer_product_counts[i] + 1, 0);

        std::fill(temp_counts.begin(), temp_counts.end(), 0);
        int index = 0, offset = best.location_of(offer_product_counts);
        do {
            best[index + offset] = std::min(best[index + offset], best[index] + special_offer.second);
        } while (next_cartesian_product(temp_counts, ranges, index, best.element_size));
    }

    out << best.data.back() << '\n';

    in.close();
    out.close();
}
