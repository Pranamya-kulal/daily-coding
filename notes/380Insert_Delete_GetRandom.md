# 🎲 LeetCode 380 - Insert Delete GetRandom O(1)

🔗 **Problem Link:** [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/description/?envType=study-plan-v2&envId=top-interview-150)

---

## 🧠 Problem Summary

Design a data structure that supports these operations in **average O(1)** time:

| Method         | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `insert(val)`  | Inserts `val` if not present. Returns `true` if inserted, `false` otherwise.|
| `remove(val)`  | Removes `val` if present. Returns `true` if removed, `false` otherwise.     |
| `getRandom()`  | Returns a random element from the current set. Each has equal probability.  |

🔹 Constraints:
- At most 2 × 10⁵ calls to the functions.
- `getRandom()` is only called when the set is not empty.

---

## 🔧 Data Structures Used

```cpp
unordered_map<int, int> mp; // Maps value ➜ index in vector
vector<int> vals;           // Stores the actual values
```

### Why this combo?

| Task        | Structure Used    | Why?                                |
|-------------|-------------------|-------------------------------------|
| Fast lookup | `unordered_map`   | O(1) search for existence           |
| Fast insert | `vector` + map    | Push to end, map stores index       |
| Fast delete | `vector` + map    | Swap with last element & pop_back   |
| Random pick | `vector`          | Access by index                     |

---

## ✅ Full Code (C++)

```cpp
class RandomizedSet {
public:
    unordered_map<int, int> mp;  // val ➜ index in vector
    vector<int> vals;            // list of inserted values

    RandomizedSet() {
        // No need to initialize anything manually
    }

    bool insert(int val) {
        if (mp.find(val) != mp.end())
            return false;

        vals.push_back(val);           // Add value to end of vector
        mp[val] = vals.size() - 1;     // Map value to its index in vector
        return true;
    }

    bool remove(int val) {
        if (mp.find(val) == mp.end())
            return false;

        int idx = mp[val];             // Get index of val
        int lastVal = vals.back();     // Get last value in vector

        vals[idx] = lastVal;           // Overwrite val with lastVal
        mp[lastVal] = idx;             // Update lastVal's index in map

        vals.pop_back();               // Remove last element
        mp.erase(val);                 // Remove val from map

        return true;
    }

    int getRandom() {
        int randIndex = rand() % vals.size();
        return vals[randIndex];        // Return value at random index
    }
};
```

---

## 🧠 Step-by-Step Breakdown

### 🔹 Constructor
```cpp
RandomizedSet() {
    // Nothing to initialize — map and vector are empty by default
}
```

---

### 🔹 insert(val)

```cpp
if (mp.find(val) != mp.end()) return false;
```
- `mp.find(val)` checks if `val` exists.
- If it **does**, return `false`.

```cpp
vals.push_back(val);
mp[val] = vals.size() - 1;
```
- Add the value at the **end of vector**.
- Store its index in the map.

---

### 🔹 remove(val)

```cpp
if (mp.find(val) == mp.end()) return false;
```
- If the value doesn’t exist, return `false`.

```cpp
int idx = mp[val];
int lastVal = vals.back();
```
- Get the index of the value we want to remove.
- Get the last value from the vector.

```cpp
vals[idx] = lastVal;
mp[lastVal] = idx;
```
- Move the last value to the spot of the removed value.
- Update the index in the map.

```cpp
vals.pop_back();
mp.erase(val);
```
- Remove the last value (we already moved it).
- Erase `val` from the map.

---

### 🔹 getRandom()

```cpp
int randIndex = rand() % vals.size();
return vals[randIndex];
```
- Get a random index from 0 to size-1
- Return the value at that index in vector

---

## 🧪 Example Execution

### Input:
```
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
```

### Output:
```
[null, true, false, true, 2, true, false, 2]
```

---

## 🧠 Concept to Remember

- `mp.find(val)` checks if the key exists.
- If not found, returns `mp.end()`.
- `vals.push_back(val)` adds at end.
- `vals.pop_back()` removes last element.
- `getRandom()` uses `rand() % size` to pick index.

---

## ✅ Time & Space Complexity

| Operation    | Time   | Space |
|--------------|--------|--------|
| insert()     | O(1)   | O(n)   |
| remove()     | O(1)   | O(n)   |
| getRandom()  | O(1)   | O(n)   |

---

## 📚 Summary

Use a combo of:
- `unordered_map` for fast lookups and indexing
- `vector` for fast inserts, deletes (with trick), and random access

This lets all 3 operations run in average **O(1)** time!
