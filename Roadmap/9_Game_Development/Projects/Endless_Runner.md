# **Project: Endless Runner (Game Dev)**

Think of games like *Dino Run* (the Chrome offline game) or *Flappy Bird*. This project teaches you about **Infinite Spawning** and **Object Pooling**.

---

## **1. Requirements**
- **Player:** Can jump to avoid obstacles.
- **Obstacles:** Spawn randomly on the right and move to the left.
- **Score:** Increases as the player stays alive.
- **Game Over:** Happens if the player hits an obstacle.

---

## **2. Tech Stack**
- **Engine:** Godot (GDScript) or Raylib (C++).
- **Hardware Impact:** Very low. Runs great on your i3 laptop.

---

## **3. Key Concept: Parallax Scrolling**
To make it feel like the player is moving, you don't move the player; you move the **Background** in the opposite direction.
- Fast background = Fast movement feel.

---

## **4. Step-by-Step Build**
1. **Player:** Add a sprite with a `KinematicBody2D` and a "Jump" script.
2. **Spawner:** Create a script that creates a new obstacle every 2 seconds.
3. **Collision:** Add `Area2D` to the obstacles to detect hits.
4. **UI:** Add a `Label` to track the high score.

---

## **🎯 Challenge for You:**
Add **Power-ups** (like a Shield or a Speed Boost) that spawn occasionally.
