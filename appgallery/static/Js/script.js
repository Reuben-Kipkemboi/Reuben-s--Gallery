  $(document).ready(function () {
      $("#MyModal").modal();
      $('#myModal').on('shown.bs.modal', function () {
          $('#myInput').focus();
      });
    });

    function copyFunction() {
        //  Get the text field by its id
        let copiedLinkText = document.getElementById("input");

        //   copy text inside the readonly input field
        navigator.clipboard.writeText(copiedLinkText.value);
      
        /* Alert the copied text */
        alert("Successfully copied the link.Now share your favourite image:" + copiedLinkText.value);
      }