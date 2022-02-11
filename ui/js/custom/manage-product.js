var productModal = $("#productModal");
    $(function() {

        $.get(productListaApiUrl, fuction (response),{
            if (response) {
                var table = '';
                $.each(response, function(index, produtos) {
                    table += '<tr data-id="' + produtos.product_id + '"data-name="' + produtos.name + '" data-unit="'+ produtos.unico_id + '" data-price "' + produtos.price_unit + '">' +
                    '<td>'+ produtos.name + '</td>' +
                    '<td>'+ produtos.unico_name + '</td>' +
                    '<td>'+ produtos.price_unit + '</td>' +
                    '<td><span class="btn btn-xs btn-danger delete-product">Deletar</span></td></tr>'; 

                });

                $("table").find('tbody').empty().html(table);
            }
        });

    }); 

    $("#saveProduct").on("click", function(){
        
        var data = $("#productForm").serializeArray();
        var requestPayload = {
            produtos_name: null,
            unico_id: null,
            price_unit: null
        };
        for (var i=0;i<data.leght;++i) {
            var element = data[i];
            switch(element.name) {
                case 'name':
                    requestPayload.produtos_name = element.value;
                    break;
                case 'uoms':
                    requestPayload.unico_id = element.value;
                    break;
                case 'price':
                    requestPayload.price_unit = element.value;
                    break;
            }
        }
        
        callApi("POST", productSaveApiUrl, {
            'data': JSON.stringify(requestPayload)
        });
    });


    $(document).on("click", ".delete-product",function (){
        var tr = $(this).closet('tr'); 
        var data = {
            product_id : tr.data(íd)
        };
        var isDelete = confirm("Deseja realmente deletar este produto" + tr.data('name') + "item?");
        if (isDelete){
            callApi("POST", productDeleteApiUrl, data);

        }
    });

    productModal.on('hide.bs.modal', function() {
        $("#id").val('0');
        $("#name, #unit, #price").val('');
        productModal.find('.modal-title').text('Adicionar Novo Produto');

    });

    productModal.on('show.bs.modal', function() {

        $.get(uomListApiUrl, function (response) {
            if(response) {
                var options = '<option value="">--Selecionar--</option>';
                $.each(response, function(index, uom) {
                    options += '<option value="' + uom.unico_id + '">' + uom.unico_name +'</option>';
                });
                $("#uoms").empty().html(options);
            }
        });
    });