# **Phase 9: Game Development - Fundamentals**

Game development is the intersection of high-performance coding, mathematics, and art.

---

## **1. Language Choice: C++ and C#**

### **C++ (The Performance King)**
- Used in **Unreal Engine** and for building custom engines.
- Requires deep understanding of **Memory Management** (Pointers, References).
- **Tool Recommendation:** **Raylib**. It's a tiny C++ library that lets you build games without a heavy editor. Perfect for your i3 laptop!

### **C# (The Industry Favorite)**
- Used in **Unity** and **Godot**.
- Easier to learn than C++ but still powerful.

---

## **2. Game Math: Vectors & Physics**

- 📐 [Vectors & Physics Math Deep Dive](./Math/Vectors_and_Physics.md)

You don't need to be a math genius, but you need to understand:
- **Vectors:** Position, Velocity, and Acceleration. (e.g., `Position = Position + Velocity`).
- **Collision Detection:** How to tell if a bullet hit a player (AABB - Axis-Aligned Bounding Box).
- **Delta Time:** Making sure your game runs at the same speed on a slow laptop and a fast PC.
- 🏀 [Game Physics Basics](./Math/Game_Physics_Basics.md)

---

## **3. The Game Loop**

Every game runs in a loop:
1. **Input:** Did the player press 'Space'?
2. **Update:** Move the player up.
3. **Render:** Draw the player at the new position on the screen.

---

## **4. 2D vs 3D**

- **Start with 2D:** It's much easier to learn the logic of game states, sprites, and basic physics in 2D.
- **Move to 3D:** Once you understand 2D, you add a Z-axis and learn about Shaders, Lighting, and 3D Meshes.

---

## **🚀 Mini-Projects for Practice**
- 🎮 [Endless Runner (Game Dev)](./Projects/Endless_Runner.md)
- 👾 [Space Invaders Clone](./Projects/Space_Invaders_Clone.md)

## **🎯 Exercise for You:**
Using **Pygame** or **Raylib**, build a simple **Pong** game.
- Two paddles, one ball.
- Score tracking.
- Increasing ball speed over time.

[Next Step: Lightweight Engines (Godot & Raylib) ->](./Lightweight_Engines.md)
