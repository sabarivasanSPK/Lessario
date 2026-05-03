# **Project: Weather Forecast App (Mobile)**

Connect to a real-world API to show live weather data for any city.

---

## **1. Requirements**
- **Search City:** Input field to type a city name.
- **Current Weather:** Show Temperature, Humidity, and Condition (e.g., "Sunny").
- **7-Day Forecast:** A list showing the predicted weather for the next week.
- **Dynamic Icons:** Show a sun icon for clear sky, cloud for overcast, etc.

---

## **2. Tech Stack**
- **API:** [OpenWeatherMap](https://openweathermap.org/api) (Free Tier).
- **Android:** Retrofit + GSON.
- **Flutter:** Http package + JSON Serializable.

---

## **3. Key Concept: Networking & JSON Parsing**
Most mobile apps are just "frontends for APIs." 
1. **Request:** Send a city name to the API.
2. **Response:** Receive a large JSON string.
3. **Parsing:** Convert that JSON into your app's objects (e.g., a `Weather` class).

---

## **4. Step-by-Step Build**
1. **API Key:** Sign up for OpenWeatherMap and get your free key.
2. **Network Layer:** Write a function to fetch data from the URL.
3. **Parsing:** Map the JSON fields to your Kotlin/Dart variables.
4. **UI:** Create a beautiful, weather-themed background that changes based on the condition.

---

## **🎯 Challenge for You:**
Use **GPS Location** to automatically show the weather for the user's current city when they open the app.
