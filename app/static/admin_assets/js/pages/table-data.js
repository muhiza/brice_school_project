

$(document).ready(function() {
    
    "use strict";
    // Datatables
    $('#all_members').dataTable();
    $('#male_members').dataTable();
    $('#female_members').dataTable();
    $('#youth').dataTable();
    $('#applicants').dataTable();
    $('#education').dataTable();
    $('#education1').dataTable();
    $('#education2').dataTable();
    $('#education3').dataTable();
    $('#education4').dataTable();
    $('#disabilities').dataTable();
    $('#disabilities1').dataTable();
    $('#disabilities2').dataTable();
    $('#disabilities3').dataTable();
    $('#disabilities4').dataTable();
    $('#group_members').dataTable();
    $('#all_members_paid').dataTable();
    $('#all_members_half').dataTable();
    $('#all_members_zero').dataTable();

    // Stock tables.
    $('#stock_home').dataTable();
    $('#stock_umusaruro').dataTable();
    $('#stock_inyongeramusaruro').dataTable();
    $('#stock_imisanzu').dataTable();
    $('#stock_bank').dataTable();
    $('#stock_ibirarane').dataTable();
    $('#stock_ibihano').dataTable();
    $('#stock_ibindi').dataTable();
    $('#stock_imyishyurire').dataTable();


    
    
    
    var table = $('#example2').DataTable({
        "columnDefs": [
            { "visible": false, "targets": 2 }
        ],
        "order": [[ 2, 'asc' ]],
        "displayLength": 25,
        "drawCallback": function ( settings ) {
            var api = this.api();
            var rows = api.rows( {page:'current'} ).nodes();
            var last=null;
 
            api.column(2, {page:'current'} ).data().each( function ( group, i ) {
                if ( last !== group ) {
                    $(rows).eq( i ).before(
                        '<tr class="group"><td colspan="5">'+group+'</td></tr>'
                    );
 
                    last = group;
                }
            } );
        }
    } );
 
    // Order by the grouping
    $('#example2 tbody').on( 'click', 'tr.group', function () {
        var currentOrder = table.order()[0];
        if ( currentOrder[0] === 2 && currentOrder[1] === 'asc' ) {
            table.order( [ 2, 'desc' ] ).draw();
        }
        else {
            table.order( [ 2, 'asc' ] ).draw();
        }
    } );
    
    $.fn.isValid = function(){
        return this[0].checkValidity()
    }
    
    var t = $('#example3').DataTable();
 
    $('#add-row').on( 'click', function () {
        if($("#add-row-form").isValid()) {
            var name = $('#name-input').val(),
                position = $('#position-input').val(),
                age = $('#age-input').val(),
                date = $('#date-input').val(),
                salary = $('#salary-input').val();
            t.row.add( [
                name,
                position,
                age,
                date,
                '$' + salary
            ] ).draw();
            
            $('.modal').modal('hide');
            
            return false;
        }
    });
    
    $('.date-picker').datepicker({
        orientation: "top auto",
        autoclose: true
    });
});


