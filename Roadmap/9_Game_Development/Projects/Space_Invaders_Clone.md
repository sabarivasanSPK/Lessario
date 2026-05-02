# **Project: Space Invaders Clone (Game Dev)**

A classic project that teaches you about **Grid Movement**, **Projectile Logic**, and **AI States**.

---

## **1. Requirements**
- **Player Ship:** Can move left/right and shoot bullets.
- **Alien Swarm:** Moves in a grid, shifts down when hitting the edge.
- **Bullets:** Player bullets destroy aliens; alien bullets destroy the player.
- **Destructible Barriers:** (Bonus) Shields that take damage over time.

---

## **2. Tech Stack**
- **Engine:** Godot or Raylib.
- **Optimization:** Use an "Array" to keep track of all active aliens.

---

## **3. Key Concept: State Management**
The aliens have different states:
- **Moving Right.**
- **Moving Left.**
- **Moving Down.**
- **Firing.**

---

## **4. Step-by-Step Build**
1. **Player:** Set up movement and bullet spawning.
2. **Aliens:** Create one alien "Scene" and instance it 50 times in a grid.
3. **Movement Logic:** Write a script that controls the whole group.
4. **Collision:** Use tags (e.g., "Alien", "Bullet") to handle what happens when objects hit.

---

## **🎯 Challenge for You:**
Add a **"Mystery Ship"** that flies across the top of the screen occasionally for bonus points.
