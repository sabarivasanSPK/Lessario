# **Phase 11: Web3 - Solidity Fundamentals**

Solidity is the primary language for writing smart contracts on the Ethereum blockchain. It is statically typed and feels similar to JavaScript or C++.

---

## **1. A Simple Contract**
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    uint256 public storedData; // State variable

    function set(uint256 x) public {
        storedData = x;
    }

    function get() public view returns (uint256) {
        return storedData;
    }
}
```

---

## **2. Key Data Types**
- **`uint` / `int`:** Unsigned and signed integers.
- **`address`:** Holds a 20-byte Ethereum address.
- **`bool`:** Boolean (true/false).
- **`mapping`:** Similar to a Dictionary or Hashmap. `mapping(address => uint) public balances;`

---

## **3. Visibility Specifiers**
- **`public`:** Can be called by anyone.
- **`private`:** Only accessible within the current contract.
- **`view`:** A function that reads data but doesn't change it (Costs no gas!).
- **`pure`:** A function that doesn't even read data (Costs no gas!).

---

## **4. Deployment (Remix IDE)**
The easiest way to start is using [Remix IDE](https://remix.ethereum.org/). It is a browser-based tool where you can write, compile, and deploy contracts to a test network instantly.

---

## **🎯 Exercise for You:**
1. Open Remix IDE.
2. Create a file called `Counter.sol`.
3. Write a contract that has a `count` variable and two functions: `increment()` and `decrement()`.
4. Compile and deploy it to the "Remix VM."

[Next Step: DApp Architecture ->](./DApp_Architecture.md)
