const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");

const deleteModalComment = new bootstrap.Modal(document.getElementById("deleteModalComment"));
const deleteButtonComment = document.getElementsByClassName("btn-delete-comment");
const deleteConfirm = document.getElementById("deleteConfirm");

const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_text");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");
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


for (let button of editButtons) {
  button.addEventListener("click", (e) => {
  let commentId = e.target.getAttribute("data-comment_id");
  let commentContent = document.getElementById(`comment${commentId}`).innerText;
  commentText.value = commentContent;
  submitButton.innerText = "Update";
  commentForm.setAttribute("action", `edit_comment/${commentId}`);
  });
}