const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");


/**
* deletion functionality for delete confirmation button and modal.
*/

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      deleteModal.show();
    });
  }