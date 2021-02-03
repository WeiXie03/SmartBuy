$(document).ready(function() {
    var table = $("#models").DataTable();
    table.destroy();
});

$(document).ready(function() {
    //$.getJSON("/models", function(json_data) {

    var table = $("#models").DataTable( {
        "ajax": {
            "url": "/models", // This now works too thanks to @kthorngren
            "dataType": "json",
            "dataSrc": "data",
            "contentType":"application/json"
        },
        columns: [
            {"data": "model_info.0.name" },
            {"data": "cpu.model" },
            {"data": "cpu.cores" },
            {"data": "memory.size" },
            {"data": "gpu.model" },
            {"data": "display.size" },
            {"data": "total_storage_capacity" },
            // year should be 4 long
            {"data": "model_resources.launch_date" },
            {"data": "config_price" },
            {"data": "operating_system" }
        ]
    });
    $("#models").on("click", "tbody tr", function() {
        link = `/models/${table.row(this).data()['model_info'][0]['id']}`
        // console.log(link);
        console.log(table.row(this).data()['model_info'][0]['id']);
        window.location.href = link;
    } );
    $('tbody tr').css('cursor','pointer');
})

    /*
    let url = "/models"
    let table = $("#models").DataTable( {
        "processing": true,
        "ajax": url,
        columns: [
            {data: "model_info.name" },
            {data: "cpu.model" },
            {data: "cpu.cores" },
            {data: "memory.size" },
            {data: "gpu.model" },
            {data: "display.size" },
            {data: "total_storage_capacity" },
            // year should be 4 long
            {data: "model_resources.launch_date".substring(0, 5) },
            {data: "config_price" },
            {data: "operating_system" }
        ]
    }
    */
