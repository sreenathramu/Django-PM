$(document).ready(function(){
  $('.signup input').addClass('form-control')

   $('#categoryTable').DataTable();

   $('#taskTable').DataTable();

   $('#task_priority').selectpicker({
      style: 'btn-info',
      size: 4
    });

  $('#category').selectpicker({
      style: 'btn-info',
      size: 4
    });
});

function goBack() {
    window.history.back();
}

function deleteTask(taskId){
  $.ajax({
    url: "/app/delete/task",
    method : 'GET',
    dataType: "json",
    data:{"taskId":taskId},
    success: function(result){
      location.reload();
    },
    error: function(xhr){
            console.log("An error occured: " + xhr.status + " " + xhr.statusText);
    }
  });
}

function moveTask(taskId){
  $('#taskHiddenId').val(taskId);
  $('#myModal1').modal('show'); 
}

function editTask(taskId,taskPriority){
  $('#taskHiddenId_').val(taskId);
  $('#task_priority').val(taskPriority);
  $('#myModal2').modal('show'); 
}
