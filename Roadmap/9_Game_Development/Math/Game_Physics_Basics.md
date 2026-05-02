# **Game Dev: Game Physics Basics**

You don't need a PhD in physics, but you need to know how to simulate a world that "feels" right to the player.

---

## **1. Gravity and Jumping**
Gravity is just a constant downward force.
```csharp
velocity.y += gravity * delta;
position.y += velocity.y * delta;

// Jumping
if (isGrounded && inputJump) {
    velocity.y = -jumpForce;
}
```

---

## **2. Friction and Air Resistance**
Without friction, your player would slide forever like they're on ice.
```csharp
velocity.x *= 0.9f; // Reduces speed by 10% every frame
```

---

## **3. Bouncing (Restitution)**
When an object hits a wall, it should bounce back.
```csharp
if (hitWall) {
    velocity.x = -velocity.x * bounciness; // bounciness between 0 and 1
}
```

---

## **4. Frame-Rate Independence**
If your physics logic is tied to frames, the player will jump higher on a fast computer than on a slow one.
- **Always multiply by `delta`!**
- Use **Fixed Timestep** (e.g., `_physics_process` in Godot) for physics calculations.

---

## **🎯 Exercise for You:**
Implement a "Dashing" mechanic. 
1. When the player presses 'Shift', multiply their velocity by 5 for a short duration (e.g., 0.2 seconds).
2. Ensure they cannot dash again for 1 second (Cooldown).
