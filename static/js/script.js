const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");

const deleteModalComment = new bootstrap.Modal(document.getElementById("deleteModalComment"));
const deleteButtonComment = document.getElementsByClassName("btn-delete-comment");
const deleteConfirm = document.getElementById("deleteConfirm");
/**
* functionality for delete confirmation button and modal for Events.
*/

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      deleteModal.show();
    });
  }

  /**
* deletion functionality for delete confirmation button and modal for Comments.
*/

  for (let button of deleteButtonComment) {
    button.addEventListener("click", (e) => {
      let commentId = e.target.getAttribute("data-comment_id")
      deleteConfirm.href = `delete_comment/${commentId}`
      deleteModalComment.show();
    });
  }