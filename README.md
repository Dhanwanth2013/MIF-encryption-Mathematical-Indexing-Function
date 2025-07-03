# 🛡️ MIF Encryption — Mathematical Indexing Function Encryption  
### 🔐 Invented by Dhanwanth  
> *“Everything started with a normal thought in the classroom.”*

---

## 📜 Description

**MIF Encryption** is a custom encryption algorithm invented by Dhanwanth.  
It is based on a unique concept: transforming characters into numerical face values,  
applying mathematical logic, and then obscuring the result through probabilistic digit mutation and randomized separators.

Unlike traditional encryption schemes, MIF is:

- 🤯 Highly customizable  
- 🔄 Layered and modular  
- 🎲 Randomized but reproducible  
- 💡 Created from scratch with original logic

---

## 🧪 How It Works

**Input:** A string, like `"Dhanwanth"`  
**Process:**

1. **Character Indexing**  
   Each character is mapped to its position in a custom `char_set`  
   (lowercase + uppercase + punctuation + digits).  
   > `'D'` → `29`, `'h'` → `7`, `'a'` → `0`, etc.

2. **Mathematical Transformation**  
   A mathematical function is applied (default is `x²`, but can be anything).  
   > `29` → `841`, `7` → `49`, `0` → `0`

3. **Random Integer Mutation**  
   A random number (1–50) is added to each result for obfuscation.  
   > `841 + 25 = 866`

4. **Digit Character Mutation**  
   Digits are optionally replaced by corresponding characters  
   in the char set with a mutation probability.  
   > `'4'` → `'e'`, `'0'` → `'a'`, etc.

5. **Randomized Digit Separators**  
   Two-digit and three-digit numbers get randomized **between-digit** symbols.  
   > `34` → `3>4`, `406` → `4;0;6`

---

## 💻 Example

**Input: d**
   
**Encrypted Output (with seed = 0): 3>e**


---

## 🔄 Decryption

Decryption is possible **only if**:
- The random seed is preserved
- The math function (e.g., x²) is known
- Mutation and separator rules are tracked

This makes MIF great for:
- 🔐 Obfuscated secure strings
- 🧩 Puzzle/treasure hunt encryption
- 🧠 Crypto-logic mini games

---

## 🔧 Customization Options

- 🔣 Swap any math function (e.g., x², 3x+7, modulo)
- 🎭 Tune mutation probability
- 🧩 Custom separators
- 🔄 Reversible or irreversible mode
- 🧪 Debug and traceable versions

---


---

## 📣 Credit

> Invented by **Dhanwanth**  
> Implementation in python partnered by ChatGPT

---

## ✨ Quote from the Creator

> “Everything started with a normal thought in the classroom.”  
> — **Dhanwanth**, Creator of MIF Encryption a twelve year old, Indian, 8th grader

---



