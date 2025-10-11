$(document).ready(function(){

    $(".cuatri").on("change", function(){
        let cuatrimestre = $(".cuatri").val();
        $(".materia").html('<option> Cargando Materia... </option>');

            $.ajax({
                url: 'ajax/carga_materias/',
                type: 'GET',
                data: {'cuatri':cuatrimestre},
                success: function(data){
                    $(".materia").html(data);
                }
            })
        
    })

});