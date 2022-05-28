function changeBirthday(parent) {
    const value = parent.querySelector('input').value
    const birthday = new Date(value)
    const age = new Date(new Date() - birthday).getFullYear() - 1970;
    parent.querySelector('#age').innerText = age
}

function setAuthors(quantity) {
    const authors = [...document.querySelectorAll('.author')].length;
    const diff = Number(quantity) - authors;
    console.log(diff)
    for (let index = 0; index < Math.abs(diff); index++) {
        if (diff > 0)
            appendAuthor()
        else {
            popAuthor()
        }
    }
    document.querySelector("button").disabled = authors === 0;
}

function appendAuthor() {
    const template = document.querySelector(".template");
    const clone = template.cloneNode(true);
    clone.classList.remove("template")
    clone.classList.remove("visually-hidden")
    clone.classList.add("author")
    const authors = document.querySelector(".authors");
    authors.appendChild(clone)
}

function popAuthor() {
    [...document.querySelectorAll(".author")].at(-1).remove();
}
