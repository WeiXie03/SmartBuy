$(document).ready(function() {
    $.getJSON("/data", function(data, status, xhr){
        $("#result").html(data['0']['0']);
    })
})
