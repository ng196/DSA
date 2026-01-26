class Solution {
public:
    void remove(int i, vector<int>& arr) {
        while (!arr.empty()) {
            int last = arr.back();

            if (last < 0) {
                break;
            }

            if (last == i) {
                arr.pop_back();
                return;
            }

            if (last > i) {
                return;
            }

            if (last < i) {
                arr.pop_back();
            }
        }
        arr.push_back(-1 * i);
    }

    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> arr;
        int n = asteroids.size();

        for (int i = 0; i < n; i++) {
            if (asteroids[i] < 0) {
                remove(abs(asteroids[i]), arr);
            } else {
                arr.push_back(asteroids[i]);
            }
        }
        return arr;
    }
};