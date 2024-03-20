const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* deletion functionality for delete confirmation button and modal.
*/

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let eventId = e.target.getAttribute("event_id");
      deleteConfirm.href = `event/${eventId}/delete/`;
      deleteModal.show();
    });
  }