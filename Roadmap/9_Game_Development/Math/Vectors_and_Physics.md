# **Game Dev: Vectors & Physics Math**

Games are essentially math in motion. To move a character or bounce a ball, you need to understand vectors.

---

## **1. Vectors: Direction & Magnitude**
A Vector (in 2D) has an `x` and `y` component.
- **Position:** Where an object is. `(5, 10)`
- **Velocity:** Where an object is going and how fast. `(2, 0)` means moving right at 2 units/sec.

### **The Basic Motion Equation:**
```csharp
Position = Position + (Velocity * DeltaTime);
```
*`DeltaTime` ensures the game runs at the same speed regardless of the frame rate.*

---

## **2. Normalization**
Making a vector have a length of 1. Useful for directions (e.g., "North-East" should have the same speed as "North").

---

## **3. Collision Detection (AABB)**
Axis-Aligned Bounding Box is the simplest way to check if two rectangles overlap.
```csharp
if (rect1.x < rect2.x + rect2.width &&
    rect1.x + rect1.width > rect2.x &&
    rect1.y < rect2.y + rect2.height &&
    rect1.y + rect1.height > rect2.y) {
    // COLLISION!
}
```

---

## **4. Gravity & Friction**
- **Gravity:** A constant downward acceleration. `Velocity.y = Velocity.y + Gravity`.
- **Friction:** Slowing down an object over time. `Velocity = Velocity * 0.95`.

---

## **🎯 Exercise for You:**
Calculate the new position of a player who starts at `(0, 0)`, has a velocity of `(5, 5)`, and travels for 2 seconds with a `DeltaTime` of `0.016` (60 FPS).
