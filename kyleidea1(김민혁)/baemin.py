#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <climits>
#include <bitset>

using namespace std;

struct Order {
    int sx, sy, ex, ey;
};

int manhattan_distance(int x1, int y1, int x2, int y2) {
    return abs(x1 - x2) + abs(y1 - y2);
}

vector<Order> orders;
vector<vector<int>> dp;
vector<vector<int>> parent;
int n;

int solve(int mask, int pos, int cx, int cy, int pickups) {
    if (mask == (1 << (2 * n)) - 1) {
        return 0;
    }

    if (dp[mask][pickups] != -1) {
        return dp[mask][pickups];
    }

    int min_distance = INT_MAX;

    for (int i = 0; i < n; ++i) {
        int pick_up = 2 * i;
        int drop_off = 2 * i + 1;

        if (!(mask & (1 << pick_up)) && pickups < 2) { // Pick up
            int distance = manhattan_distance(cx, cy, orders[i].sx, orders[i].sy);
            int new_distance = distance + solve(mask | (1 << pick_up), pick_up, orders[i].sx, orders[i].sy, pickups + 1);
            if (new_distance < min_distance) {
                min_distance = new_distance;
                parent[mask][pickups] = pick_up;
            }
        } else if (!(mask & (1 << drop_off)) && (mask & (1 << pick_up)) && pickups > 0) { // Drop off
            int distance = manhattan_distance(cx, cy, orders[i].ex, orders[i].ey);
            int new_distance = distance + solve(mask | (1 << drop_off), drop_off, orders[i].ex, orders[i].ey, pickups - 1);
            if (new_distance < min_distance) {
                min_distance = new_distance;
                parent[mask][pickups] = drop_off;
            }
        }
    }

    return dp[mask][pickups] = min_distance;
}

int main() {
    cin >> n;
    orders.resize(n);
    for (int i = 0; i < n; ++i) {
        cin >> orders[i].sx >> orders[i].sy >> orders[i].ex >> orders[i].ey;
    }

    dp.resize(1 << (2 * n), vector<int>(3, -1)); // pickups 최대 2개까지 허용
    parent.resize(1 << (2 * n), vector<int>(3, -1)); // pickups 최대 2개까지 허용

    int min_distance = solve(0, -1, 500, 500, 0);

    vector<int> optimal_route;
    int mask = 0, cx = 500, cy = 500, pickups = 0;
    while (mask != (1 << (2 * n)) - 1) {
        int next_pos = parent[mask][pickups];
        if (next_pos % 2 == 0) {
            optimal_route.push_back(next_pos / 2 + 1);
            pickups++;
        } else {
            optimal_route.push_back(-((next_pos - 1) / 2 + 1));
            pickups--;
        }
        mask |= (1 << next_pos);
        if (next_pos % 2 == 0) {
            cx = orders[next_pos / 2].sx;
            cy = orders[next_pos / 2].sy;
        } else {
            cx = orders[(next_pos - 1) / 2].ex;
            cy = orders[(next_pos - 1) / 2].ey;
        }
    }

    for (int step : optimal_route) {
        cout << step << " ";
    }
    cout << endl;
    cout << min_distance << endl;

    return 0;
}
