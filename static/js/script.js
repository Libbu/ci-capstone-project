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
* Dunctionality for delete confirmation modal for Events.
*
* - listens for a click on the delete button in event_detail 
* - and shows a modal with the option of deleting the event.
*
* - The deletion is handled by delete_event in events/views.py
*/

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      deleteModal.show();
    });
  }

/**
* Deletion functionality for delete button and modal for Comments.
*
* - retrieves associated comment ID when clicked
* - ensures action mapped to delete comment url pattern
* - displays modal to confirm user wishes to delete comment
*/

for (let button of deleteButtonComment) {
    button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("data-comment_id")
    deleteConfirm.href = `delete_comment/${commentId}`
    deleteModalComment.show();
  });
}

/* Edit functionality for edit button in comments.
*
* - retrieves associated comment ID when clicked
* - populates CommentForm with conents of existing comment
* - changes submit button text to read 'update'
* - ensures action mapped to edit_comment url pattern
*/

for (let button of editButtons) {
  button.addEventListener("click", (e) => {
  let commentId = e.target.getAttribute("data-comment_id");
  let commentContent = document.getElementById(`comment${commentId}`).innerText;
  commentText.value = commentContent;
  submitButton.innerText = "Update";
  commentForm.setAttribute("action", `edit_comment/${commentId}`);
  });
}