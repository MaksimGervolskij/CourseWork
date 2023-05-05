function getPages() {
  const pages = document.getElementById("pages");
  const key = "console";
  fetch(`/pages/${key}/`)
    .then(response => response.json())
    .then(data => {
      pages.innerHTML = "";
      data.forEach(page => {
        const title = document.createElement("h3");
        title.textContent = page.title;
        const content = document.createElement("p");
        content.textContent = page.content;
        pages.appendChild(title);
        pages.appendChild(content);
      });
    });
}
