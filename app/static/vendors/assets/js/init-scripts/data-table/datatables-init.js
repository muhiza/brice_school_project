(function ($) {
    //    "use strict";


    /*  Data Table
    -------------*/

    $('#bootstrap-data-table').DataTable({
        lengthMenu: [[10, 20, 50, -1], [10, 20, 50, "All"]],
    });



    $('#bootstrap-data-table-one').DataTable({
        lengthMenu: [[10, 20, 50, -1], [10, 20, 50, "All"]],
    });



    $('#bootstrap-data-table-two').DataTable({
        lengthMenu: [[10, 20, 50, -1], [10, 20, 50, "All"]],
    });



    $('#bootstrap-data-table-three').DataTable({
        lengthMenu: [[10, 20, 50, -1], [10, 20, 50, "All"]],
    });



    $('#bootstrap-data-table-four').DataTable({
        lengthMenu: [[10, 20, 50, -1], [10, 20, 50, "All"]],
    });




    $('#bootstrap-data-table-five').DataTable({
        lengthMenu: [[10, 20, 50, -1], [10, 20, 50, "All"]],
    });


    $('#bootstrap-data-table-six').DataTable({
        lengthMenu: [[10, 20, 50, -1], [10, 20, 50, "All"]],
    });



    $('#bootstrap-data-table-seven').DataTable({
        lengthMenu: [[10, 20, 50, -1], [10, 20, 50, "All"]],
    });


    $('#bootstrap-data-table-eight').DataTable({
        lengthMenu: [[10, 20, 50, -1], [10, 20, 50, "All"]],
    });


    $('#bootstrap-data-table-nine').DataTable({
        lengthMenu: [[10, 20, 50, -1], [10, 20, 50, "All"]],
    });


    $('#bootstrap-data-table-ten').DataTable({
        lengthMenu: [[10, 20, 50, -1], [10, 20, 50, "All"]],
    });


    $('#bootstrap-data-table-eleven').DataTable({
        lengthMenu: [[10, 20, 50, -1], [10, 20, 50, "All"]],
    });



    $('#bootstrap-data-table-twelve').DataTable({
        lengthMenu: [[10, 20, 50, -1], [10, 20, 50, "All"]],
    });



    $('#bootstrap-data-table-thirteen').DataTable({
        lengthMenu: [[10, 20, 50, -1], [10, 20, 50, "All"]],
    });



    $('#bootstrap-data-table-fourteen').DataTable({
        lengthMenu: [[10, 20, 50, -1], [10, 20, 50, "All"]],
    });



























    $('#bootstrap-data-table-export').DataTable({
        lengthMenu: [[10, 25, 50, -1], [10, 25, 50, "All"]],
        dom: 'Bfrtip',
        buttons: ['copy', 'csv',
                                {
                    extend: 'excel',
                    messageTop: 'Cooperative des Riziculteurs dans le Marais de Kanyonyomba.'
                    },

                     'pdf', 'print'],
        "scrollX": true
    });

    $('#row-select').DataTable( {
        initComplete: function () {
                this.api().columns().every( function () {
                    var column = this;
                    var select = $('<select class="form-control"><option value=""></option></select>')
                        .appendTo( $(column.footer()).empty() )
                        .on( 'change', function () {
                            var val = $.fn.dataTable.util.escapeRegex(
                                $(this).val()
                            );

                            column
                                .search( val ? '^'+val+'$' : '', true, false )
                                .draw();
                        } );

                    column.data().unique().sort().each( function ( d, j ) {
                        select.append( '<option value="'+d+'">'+d+'</option>' )
                    } );
                } );
            }
        } );

})(jQuery);
