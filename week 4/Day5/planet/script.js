const planets = [
    { name: "Mercury", color: "gray", moons: 0 },
    { name: "Venus", color: "orange", moons: 0 },
    { name: "Earth", color: "blue", moons: 1 },
    { name: "Mars", color: "red", moons: 2 },
    { name: "Jupiter", color: "brown", moons: 79 },
    { name: "Saturn", color: "yellow", moons: 82 },
    { name: "Uranus", color: "lightblue", moons: 27 },
    { name: "Neptune", color: "darkblue", moons: 14 },
  ];
  
  const section = document.querySelector(".listPlanets");
  
  planets.forEach((planet) => {
    const planetDiv = document.createElement("div");
    planetDiv.classList.add("planet");
    planetDiv.style.backgroundColor = planet.color;
  
    const planetName = document.createElement("span");
    planetName.textContent = planet.name;
  
    planetDiv.appendChild(planetName);
  
    for (let i = 0; i < planet.moons; i++) {
      const moonDiv = document.createElement("div");
      moonDiv.classList.add("moon");
      planetDiv.appendChild(moonDiv);
    }
  
    section.appendChild(planetDiv);
  });