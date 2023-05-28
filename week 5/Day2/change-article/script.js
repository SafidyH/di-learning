 const h1Element = document.querySelector("h1");
 console.log(h1Element);

 const article = document.querySelector("article");
 const paragraphs = article.querySelectorAll("p");
 const lastParagraph = paragraphs[paragraphs.length - 1];
 lastParagraph.remove();

 const h2Element = document.getElementById("h2-chocolate");
 h2Element.addEventListener("click", function() {
   h2Element.style.backgroundColor = "red";
 });

 const h3Element = document.getElementById("h3-history");
 h3Element.addEventListener("click", function() {
   h3Element.style.display = "none";
 });

 const boldButton = document.getElementById("bold-button");
 boldButton.addEventListener("click", function() {
   paragraphs.forEach(function(paragraph) {
     paragraph.style.fontWeight = "bold";
   });
 });

 h1Element.addEventListener("mouseover", function() {
   const randomSize = Math.floor(Math.random() * 101);
   h1Element.style.fontSize = `${randomSize}px`;
 });

 const secondParagraph = paragraphs[1];
 secondParagraph.addEventListener("mouseover", function() {
   secondParagraph.classList.add("fade-out");
 });