document.querySelectorAll("form [btn_ref]").forEach((elm) => {
  const div = document.createElement("div");
  div.innerHTML = `
  <a href="${elm.getAttribute("btn_ref")}" class="btn btn-warning mt-3">Add</a>
  `;
  div.classList.add("text-end");
  elm.parentNode.insertBefore(div, elm.nextSibling);
});
