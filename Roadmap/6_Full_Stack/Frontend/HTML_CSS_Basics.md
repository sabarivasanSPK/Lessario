# **Full Stack: HTML5 & CSS3 Mastery**

Before you can build complex web apps, you must master the structure and styling of the web.

---

## **1. Semantic HTML5**
Semantic HTML tells the browser (and search engines) what the content **is**, not just how it looks.

| Tag | Purpose |
| :--- | :--- |
| `<header>` | Introductory content or navigation links. |
| `<main>` | The primary content of the body. |
| `<section>` | A thematic grouping of content. |
| `<article>` | Self-contained, independent content. |
| `<aside>` | Content indirectly related to the main content (sidebars). |
| `<footer>` | Author info, copyright, or links. |

---

## **2. CSS3 Layouts: Flexbox & Grid**

### **Flexbox (The 1D Layout)**
Best for rows or columns.
```css
.container {
    display: flex;
    justify-content: space-between; /* Horizontal alignment */
    align-items: center;            /* Vertical alignment */
}
```

### **CSS Grid (The 2D Layout)**
Best for full page layouts.
```css
.grid-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr); /* 3 equal columns */
    gap: 20px;
}
```

---

## **3. CSS Variables (Theming)**
Essential for "Dark Mode" features.
```css
:root {
    --primary-color: #f60; /* Zoho Orange */
    --bg-color: #ffffff;
}

body {
    background-color: var(--bg-color);
    color: var(--primary-color);
}
```

---

## **🎯 Exercise for You:**
Create a **Product Card** for a Zoho product (like Zoho CRM).
- Use a semantic `<article>` tag.
- Use **Flexbox** to align the product name and price.
- Use **CSS Variables** for the colors.
