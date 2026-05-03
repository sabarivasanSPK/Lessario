# **Game Dev: Godot & GDScript**

GDScript is the primary language of Godot. It’s designed specifically for game logic and is very similar to Python.

---

## **1. Nodes and Scripts**
In Godot, everything is a **Node**. You attach a script to a node to give it behavior.

```gdscript
extends Sprite2D

var speed = 400

func _process(delta):
    var velocity = Vector2.ZERO
    if Input.is_action_pressed("ui_right"):
        velocity.x += 1
    position += velocity * speed * delta
```

---

## **2. Signals (Communication)**
Signals are how nodes talk to each other without being tightly coupled.
- *Example:* A "Health" node emits a `dead` signal, and the "GameUI" node listens to it to show the "Game Over" screen.

---

## **3. The `delta` Parameter**
Always multiply your movement by `delta`!
- `delta` is the time elapsed since the last frame.
- It ensures your player moves at the same speed whether the computer is running at 30 FPS or 300 FPS.

---

## **4. Why Godot is great for your i3 Laptop?**
- It doesn't need a massive install.
- The editor is extremely snappy.
- It doesn't use heavy background processes while idle.

---

## **🎯 Exercise for You:**
Build a "Player" character that can move in 4 directions (Up, Down, Left, Right) using Godot and GDScript.
