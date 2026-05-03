# **Phase 11: Web3 - DApp Architecture**

A DApp (Decentralized Application) consists of a traditional Frontend and a Blockchain Backend.

---

## **1. The Stack**
- **Frontend:** React, Vue, or Vanilla JS.
- **Provider:** A service that connects your app to the blockchain (e.g., Infura, Alchemy, or the user's MetaMask).
- **Library:** **Ethers.js** or **Web3.js**. These are the "Axios of Web3."
- **Smart Contract:** Your backend logic living on the blockchain.

---

## **2. Connecting to MetaMask**
In your React app, you need to "Request Accounts" from the user.
```javascript
const provider = new ethers.providers.Web3Provider(window.ethereum);
await provider.send("eth_requestAccounts", []);
const signer = provider.getSigner();
```

---

## **3. Interacting with a Contract**
To talk to a contract, you need two things:
1. **Contract Address:** Where it is deployed.
2. **ABI (Application Binary Interface):** A JSON file that describes the contract's functions.

```javascript
const contract = new ethers.Contract(address, abi, signer);
const tx = await contract.set(42); // Sending a transaction
await tx.wait(); // Wait for it to be mined
```

---

## **4. Event Listening**
Smart contracts can emit events (like "NewTransaction"). Your frontend can listen for these events to update the UI in real-time.

---

## **🎯 Exercise for You:**
Build a simple webpage that:
1. Has a "Connect Wallet" button.
2. Displays the user's Ethereum address once connected.
3. Shows the user's current ETH balance.

[Next Step: Web3 Mini-Projects ->](./Projects.md)
