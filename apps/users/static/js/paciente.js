$(document).ready(function(){

    $('#editar-paciente-modal').on('show.bs.modal', function(event){

        var modal = $(this);
        var link = $(event.relatedTarget);

        var id = link.data('id');
        var nombre = link.data('nombre');
        var apellido = link.data('apellido');
        var dui = link.data('dui');


        modal.find('.modal-body #id-prueba').val(id);
        modal.find('.modal-body #nombre-edit').val(nombre);
        modal.find('.modal-body #apellido-edit').val(apellido);
        modal.find('.modal-body #dui-edit').val(dui);
        modal.find('.modal-body #fecha-edit').val(fecha);
    });


})