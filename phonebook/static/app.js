const searchBar = document.querySelector(".search");
const tableBody = document.querySelector("#tbody");
const contacts = {
    first_names: document.querySelectorAll("#first_name"),
    last_names: document.querySelectorAll("#last_name"),
};

searchBar.addEventListener("input", doSearch);

function doSearch(e) {
    // if ((e.target.value = "")) {
    //     location.reload();
    // }
    for (let i = 0; i < contacts.first_names.length; i++) {
        if (
            contacts.first_names[i].textContent
                .trim()
                .indexOf(e.target.value) === -1 &&
            contacts.last_names[i].textContent
                .trim()
                .indexOf(e.target.value) === -1
        ) {
            contacts.first_names[i].parentElement.style.display = "none";
        } else {
            contacts.first_names[i].parentElement.style.display = "inherit";
        }
    }
}
