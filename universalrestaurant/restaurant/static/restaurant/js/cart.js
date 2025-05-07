document.addEventListener('DOMContentLoaded', function () {
    $(document).ready(function () {

        $(document).on("click", "#closeModalBtn", function () {
            $("#cartModal").hide();
        });

        $(document).on("click", '.add-to-cart', function (e) {
            e.preventDefault();

            var goodsInCartCount = $('#goods-in-cart-count');
            var cartCount = parseInt(goodsInCartCount.text() || 0);

            var dish_id = $(this).data("dish-id");
            var add_to_cart_url = $(this).attr("href");

            $.ajax({
                type: "POST",
                url: add_to_cart_url,
                data: {
                    dish_id: dish_id,
                    csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
                },
                success: function (data) {
                    cartCount++;
                    goodsInCartCount.text(cartCount);

                    var CartItemContainer = $("#cartModal");
                    CartItemContainer.html(data.cartModal);
                }
            });
        });

        $(document).on("click", ".remove_from_cart", function (e) {
            e.preventDefault();

            var DishesInCartCount = $('#goods-in-cart-count');
            var cartCount = parseInt(DishesInCartCount.text() || 0);

            var cart_id = $(this).data('cart-id');
            var remove_from_cart_url = $(this).attr("href");

            $.ajax({
                type: "POST",
                url: remove_from_cart_url,
                data: {
                    cart_id: cart_id,
                    csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
                },
                success: function (data) {
                    cartCount -= data.quantity_deleted;
                    DishesInCartCount.text(cartCount);

                    var CartItemContainer = $("#cartModal");
                    CartItemContainer.html(data.html_context);
                }
            });
        });

        $(document).on("click", ".sub_div", function (){
            var url = $(this).data("cart-change-url");
            var cartID = $(this).data("cart-id");
            var $input = $(this).closest('.input-group').find('.number');
            var currentValue = parseInt($input.val());

            if (currentValue>1){
                $input.val(currentValue-1);
                updateCart(cartID, currentValue - 1, -1, url);
            }


        });


        $(document).on("click", ".add_div", function (){
            var url = $(this).data("cart-change-url");
            var cartID = $(this).data("cart-id");
            var $input = $(this).closest('.input-group').find('.number');
            var currentValue = parseInt($input.val());


            $input.val(currentValue+1);
            updateCart(cartID, currentValue + 1, 1, url);


        });

        function updateCart(cartID, quantity, change, url){
            $.ajax({
                type:"POST",
                url:url,
                data: {
                    cartID: cartID,
                    quantity: quantity,
                    csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
                },

                success: function (data){
                    var DishesInCartCount = $('#goods-in-cart-count');
                    var cartCount = parseInt(DishesInCartCount.text() || 0);
                    cartCount += change;
                    DishesInCartCount.text(cartCount);
                    var CartItemContainer = $("#cartModal");
                    CartItemContainer.html(data.html_context);
                }

            })
        }

    });
});
