# **Phase 9: Game Development - Lightweight Engines**

Since you are working on 8GB of RAM and an i3 processor, heavy engines like Unreal Engine 5 will be very frustrating. These engines are powerful but light enough to run smoothly on your device.

---

## **1. Godot Engine (Highly Recommended)**

- 🎮 [Godot & GDScript Deep Dive](./Godot_GDScript.md)

Godot is the best "all-in-one" engine for your hardware.
- **Size:** ~100MB (Unreal is 100GB+).
- **Languages:** GDScript (like Python) or C#.
- **Features:** Great 2D and capable 3D support.
- **Hardware Impact:** Runs very well on 8GB RAM.

---

## **2. Raylib (For the C++ Purists)**

Raylib is not a full "Engine" with a GUI; it's a code library. 
- **Pros:** Extremely fast, uses almost zero RAM, and teaches you how games work at a low level.
- **Best for:** Learning C++ while making games.

---

## **3. Unity (The Industry Standard)**

Unity can run on your laptop, but it will be slower than Godot.
- **Optimization Tip:** Disable the "Global Illumination" and "Auto Refresh" in the editor to save CPU/RAM.
- **Use Case:** If you want to work for a major game studio, Unity is the most common requirement.

---

## **4. Why Not Unreal Engine 5?**
UE5 uses **Nanite** and **Lumen**, which require a dedicated GPU and at least 16GB (ideally 32GB) of RAM. On an i3-N305, it will likely crash or run at 1 frame per second. **Save this for after your hardware upgrade.**

---

## **🎯 Exercise for You:**
Download **Godot** and follow the "Your First 2D Game" tutorial on their official documentation. It will teach you about Nodes, Scenes, and basic GDScript.

[Back to Master Index ->](../../Zoho%20Software%20Engineer%20Preparation%20Roadmap.md)
